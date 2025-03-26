from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST
from decimal import Decimal
from .forms import OrderForm
from .models import Order, OrderLineMenu
from menu.models import MenuItem
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Cache the checkout data by updating the Stripe PaymentIntent metadata.

    This view updates the metadata of a Stripe PaymentIntent with information
    such as the cart data, delivery method, and user details. It is triggered
    by a POST request and modifies the PaymentIntent using the provided
    `client_secret`.

    **Arguments:**
    - `request`: The HttpRequest object containing POST data.

    Returns an HTTP response with status 200 on success, or status 400 with an
    error message if an exception occurs.
    """
    try:
        delivery_method = request.POST.get('delivery_method', 'not_specified')

        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'delivery_method': delivery_method,
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Handles the checkout process for an order, including processing the order
    form, calculating delivery costs and integrating with Stripe for payment.

    If the request method is POST:
    - Retrieves the cart data from the session and processes the order form.
    - Saves the order details including customer information, delivery method
    and payment details.
    - Calculates the delivery cost based on the total value of the cart and the
    delivery method selected.
    - Creates an OrderLineMenu entry for each item in the cart.
    - If the order form is valid, the order is saved and the user is redirected
    to the  checkout success page.
    - If the form is invalid, errors are displayed, and the user is prompted to
    correct the information.

    If the request method is GET:
    - Displays the checkout page with a pre-filled order form, if available and
    retrieves a Stripe payment intent.
    - Prepares Stripe for the payment process and handles any missing keys or
    required  information.
    - Provides the order form with the necessary data, including default values
    for authenticated users.

    **Arguments:**
    - `request`: The HttpRequest object, containing the user's order form data,
    cart data and Stripe payment intent details.

    Returns an HTTP response:
    - Redirects to the checkout success page if the order is processed
    successfully.
    - Re-renders the checkout page if there are form errors.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    delivery_cost = 0

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'delivery_method': request.POST.get('delivery_method', 'delivery'),
            'street_address': request.POST['street_address'],
            'town_or_city': request.POST['town_or_city'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }

        # Save delivery method in session
        request.session['delivery_method'] = form_data['delivery_method']
        request.session.modified = True  # Make sure the session updates

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)

            # Calculate total and delivery cost
            current_cart = cart_contents(request)
            total = current_cart['total']
            delivery_method = form_data['delivery_method']

            # Check delivery method and calculate delivery cost
            if delivery_method == 'delivery':
                if total < settings.FREE_DELIVERY_THRESHOLD:
                    delivery_cost = total * Decimal(
                        settings.STANDARD_DELIVERY_PERCENTAGE / 100)
                else:
                    delivery_cost = 0
            else:
                delivery_cost = 0

            grand_total = total + delivery_cost

            # Store delivery cost and method for Stripe
            order.delivery_method = delivery_method
            order.delivery_cost = delivery_cost
            order.grand_total = grand_total

            order.save()

            # Create OrderLineMenu for each cart item
            for item_id, item_data in cart.items():
                try:
                    item = MenuItem.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_menu = OrderLineMenu(
                            order=order,
                            menu=item,
                            quantity=item_data,
                        )
                        order_line_menu.save()
                except MenuItem.DoesNotExist:
                    messages.error(request, (
                        "One of the menus in cart wasn't found in database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

            # Return to checkout page with the form data and errors
            template = 'checkout/checkout.html'
            context = {
                'order_form': order_form,
                'stripe_public_key': stripe_public_key,
                'client_secret': stripe.api_key,
            }
            return render(request, template, context)

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart")
            return redirect(reverse('menu'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            metadata={
                'cart': json.dumps(cart),
                'delivery_method': request.session.get(
                    'delivery_method', 'delivery'),
                'delivery_cost': str(delivery_cost),
            })

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                   'full_name': profile.user.get_full_name(),
                   'email': profile.user.email,
                   'phone_number': profile.default_phone_number,
                   'street_address': profile.default_street_address,
                   'town_or_city': profile.default_town_or_city or 'Gothenburg',
                   'country': profile.default_country or 'SE',
                   'postcode': profile.default_postcode,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm(initial={
                'country': 'SE',
                'town_or_city': 'Gothenburg',
            })

        if not stripe_public_key:
            messages.warning(
                request, "Stripe public key is missing."
                "Did you forgot to set it to your environment?")

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handles the successful completion of a checkout process.

    When an order is successfully processed:
    - Retrieves the order details using the order number.
    - If the user is authenticated, associates the order with their user
    profile and saves any relevant profile information.
    - Optionally saves the user's information in their profile if the
    'save_info' flag is set in the session.
    - Displays a success message indicating that the order was successfully
    processed, and sends a confirmation email to the user.
    - Clears the user's cart from the session.

    **Arguments:**
    - `request`: The HttpRequest object, containing session data and user
    details.
    - `order_number`: The unique identifier for the order to be processed.

    Returns an HTTP response:
    - Renders the checkout success page with the order details.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the User's infomation
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_email': order.email,
                'default_phone_number': order.phone_number,
                'default_street_address': order.street_address,
                'default_town_or_city': order.town_or_city,
                'default_country': order.country,
                'default_postcode': order.postcode,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
                     A confirmation \
                     email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
