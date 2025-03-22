from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import MenuItem


def cart_contents(request):
    """
    Retrieve the contents of the shopping cart and calculate order totals.

    This function fetches the cart data stored in the session, retrieves the
    corresponding menu items from the database, and calculates the total cost,
    item count, delivery cost and grand total. If the selected delivery method
    is 'delivery', it applies the appropriate delivery charge based on the
    order total and free delivery threshold.

    Args:
        request (HttpRequest): The HTTP request object containing session data.

    Returns:
        dict: A dictionary containing:
            - cart_items (list): A list of dictionaries, each containing:
                - menu_id (int): The ID of the menu item.
                - quantity (int): The quantity of the item in the cart.
                - menu (MenuItem): The corresponding MenuItem instance.
            - total (Decimal): The total cost of all items before delivery
            charges.
            - item_count (int): The total number of items in the cart.
            - delivery_cost (Decimal): The calculated delivery cost.
            - free_delivery_delta (Decimal): The remaining amount needed to
            qualify for free delivery.
            - free_delivery_threshold (Decimal): The minimum order amount
            required for free delivery.
            - standard_delivery_percentage (Decimal): The percentage used to
            calculate delivery cost.
            - grand_total (Decimal): The final total.
    """

    cart_items = []
    total = 0
    item_count = 0
    delivery_cost = 0
    cart = request.session.get('cart', {})

    for menu_id, quantity in cart.items():
        menu = get_object_or_404(MenuItem, pk=menu_id)
        total += quantity * menu.price
        item_count += quantity
        cart_items.append({
            'menu_id': menu_id,
            'quantity': quantity,
            'menu': menu,
        })

    # Check the delivery method and adjust the delivery cost
    delivery_method = request.session.get('delivery_method', 'delivery')
    if delivery_method == 'delivery':
        if total < settings.FREE_DELIVERY_THRESHOLD:
            delivery_cost = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
            free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        else:
            delivery_cost = 0
            free_delivery_delta = 0
    else:
        delivery_cost = 0
        free_delivery_delta = 0

    grand_total = total + delivery_cost

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery_cost': delivery_cost,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'standard_delivery_percentage': settings.STANDARD_DELIVERY_PERCENTAGE,
        'grand_total': grand_total,
    }

    return context
