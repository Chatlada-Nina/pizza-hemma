from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    delivery = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        free_delivery_delta = 0

    grand_total = total


    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'gran_total': grand_total,
    }

    return context
