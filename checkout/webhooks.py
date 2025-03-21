from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen for webhooks from Stripe.

    This view listens for webhook events sent by Stripe, verifies their
    signature and triggers the corresponding handler function based on the
    event type.

    Args:
    request (HttpRequest): The HTTP request object containing the webhook data
    sent by Stripe.

    Returns:
    HttpResponse: A response indicating the status of webhook processing.
    Returns a 200 OK response if the event is handled successfully, otherwise
    returns a 400 Bad Request response for invalid payloads/signature errors.

    Raises:
    stripe.error.SignatureVerificationError: Raised if the signature of the
    incoming webhook does not match the expected signature.
    ValueError: Raised if the webhook payload is invalid.
    Exception: Any other unexpected errors will return a 400 Bad Request
    response.
    """
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WH_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up a webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed':
        handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
