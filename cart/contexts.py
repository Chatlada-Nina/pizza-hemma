from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import MenuItem

def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    delivery_cost = 0
    cart = request.session.get('cart', {})

    for menu_id, quantity in cart.items():
        menu =get_object_or_404(MenuItem, pk=menu_id)
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

    grand_total = delivery_cost + total

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
