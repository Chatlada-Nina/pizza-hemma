from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from decimal import Decimal
from .models import Order, OrderLineMenu
from menu.models import MenuItem
from profiles.models import UserProfile

import stripe
import json


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        try:
            intent = event.data.object
            pid = intent.id
            cart = intent.metadata.get('cart', '{}')
            save_info = intent.get('save_info', False) == 'true'

            # Get the Charge object
            stripe_charge = None
            if intent.latest_charge:
                stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

            billing_details = getattr(stripe_charge, 'billing_details', {})
            shipping_details = getattr(intent, 'shipping', {}) or {}
            shipping_address = shipping_details.get('address', {}) or {}

            full_name = shipping_details.get('name', billing_details.get('name')) 
            email = shipping_details.get('email', billing_details.get('email'))
            if not email:
                email = "no-email@example.com"
            phone = shipping_details.get('phone', billing_details.get('phone'))
            if not phone:
                phone = "no-phone@example.com" 
            street_address = shipping_address.get('line1', '')  
            postcode = shipping_address.get('postal_code', None)

            metadata = intent.metadata  # Store metadata
            delivery_method = str(intent.metadata.get('delivery_method', 'delivery')).strip().lower()

            # Initialize delivery_cost variable
            delivery_cost = Decimal(0)

            # Recalculate grand total only if delivery cost is not provided in metadata
            cart_data = json.loads(cart) if cart else {}
            total = sum(MenuItem.objects.get(id=item_id).price * quantity for item_id, quantity in cart_data.items())

            # Only recalculate delivery cost if it's not provided in the metadata
            if delivery_cost == 0:
                if delivery_method == 'delivery':
                    if total < settings.FREE_DELIVERY_THRESHOLD:
                        delivery_cost = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
                    else:
                        delivery_cost = Decimal(0)
                else:  # If pickup
                    delivery_cost = Decimal(0)

            grand_total = round(stripe_charge.amount / 100, 2)

            # Update profile information if save_info was checked.
            profile = None
            username = intent.metadata.get('username', 'AnonymousUser')
            if username != 'AnonymousUser':
                profile = UserProfile.objects.get(user__username=username)
                if profile and save_info:
                    profile.default_full_name = full_name
                    profile.default_email = email
                    profile.default_phone_number = phone
                    profile.default_street_address = street_address
                    profile.default_town_or_city = shipping_address.get('city', 'Gothenburg')
                    profile.default_country = shipping_address.get('country', 'SE')
                    profile.default_postcode = postcode
                    profile.save()

            # Check if the order already exists
            filter_kwargs = {
                "full_name__iexact": full_name or "",
                "email__iexact": email or "",
                "phone_number__icontains": phone or "",
                "street_address__icontains": street_address or "",
                "postcode__iexact": postcode or "",
                "grand_total": grand_total,
                "original_cart": cart or "",
                "stripe_pid": pid or "",
            }

            # Remove fields that are None to prevent ValueError
            filter_kwargs = {key: value for key, value in filter_kwargs.items() if value is not None}

            # Query the database
            order = Order.objects.filter(**filter_kwargs).first()

            if order:
                self._send_confirmation_email(order)
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                    status=200)

            # Create the order if it doesn't exist
            try:
                order = Order.objects.create(
                    full_name=full_name,
                    user_profile=profile,
                    email=email,
                    phone_number=phone,
                    delivery_method=delivery_method,
                    street_address=street_address,
                    town_or_city=shipping_address.get('city', 'Gothenburg'),
                    country=shipping_address.get('country', 'SE'),
                    postcode=postcode,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order.update_total()

                for item_id, item_data in json.loads(cart).items():
                    item = MenuItem.objects.get(id=item_id)
                    OrderLineMenu.objects.create(order=order, menu=item, quantity=item_data)


                self._send_confirmation_email(order)
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | Order Created',
                    status=200)
        
            except Exception as e:
                return HttpResponse(content=f'Webhook received: {event["type"]} | ERROR: {e}', status=500)
            
        except Exception as e:
            return HttpResponse(content=f'Error handling payment intent: {e}', status=500)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        try:
            return HttpResponse(
                content= f'Webhook received: {event["type"]}',
                status=200)
        except Exception as e:
            return HttpResponse(content=f'Error handling payment failed event: {e}', status=500)