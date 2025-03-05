from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import MenuItem

def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    delivery = 0
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

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total


    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
