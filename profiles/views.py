from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """
    Display and manage the user's profile.

    This view allows the logged-in user to view and update their profile info.
    It uses the `UserProfileForm` to update the user's default contact and
    delivery information.

    **Context:**
    - `form`: A form instance that allows the user to edit their profile.
    - `orders`: A list of orders associated with the user profile.
    - `on_profile_page`: A boolean to indicate that the user is on the profile
    page.

    **Messages:**
    - Success message is displayed if the profile is successfully updated.
    - Error message is displayed if the form is invalid.

    **Template:**
    :template:`profiles/profile.html`
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, "Failed adding menu."
                                    "Please ensure the form is valid.")
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    Display details of a past order.

    This view shows the details of a previous order, given the `order_number`.
    It also sends an informational message to the user that the order
    confirmation email was sent when the order was placed.

    **Context:**
    - `order`: The order instance corresponding to the provided `order_number`.
    - `from_profile`: A boolean to indicate that the user navigated here from
    their profile.

    **Messages:**
    - Informational message about the previous order confirmation.

    **Template:**
    :template:`checkout/checkout_success.html`
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a previous confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
