from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineMenu


@receiver(post_save, sender=OrderLineMenu)
def update_on_save(sender, instance, created, **kwargs):
    """
    Signal handler update the order total after an `OrderLineMenu` instance is
    saved.

    This function is triggered by the `post_save` signal, which is sent after
    an `OrderLineMenu` instance is created or updated. It ensures that the
    related `Order` instance has its totals recalculated whenever a line item
    is added or modified.

    **Arguments:**
    - `sender`: The model class (`OrderLineMenu`) that sent the signal.
    - `instance`: The actual `OrderLineMenu` instance that was saved.
    - `created`: Boolean flag indicating whether the instance was created or
    updated.
    - `**kwargs`: Additional keyword arguments passed by the signal handler.

    The function calls the `update_total()` method of the associated `Order`
    instance to recalculate the order totals based on the updated line item.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineMenu)
def update_on_delete(sender, instance, **kwargs):
    """
    Signal handler to update the order total after an `OrderLineMenu` instance
    is deleted.

    This function is triggered by the `post_delete` signal, which is sent after
    an `OrderLineMenu` instance is deleted. It ensures that the related `Order`
    instance has its totals recalculated whenever a line item is removed from
    the order.

    **Arguments:**
    - `sender`: The model class (`OrderLineMenu`) that sent the signal.
    - `instance`: The actual `OrderLineMenu` instance that was deleted.
    - `**kwargs`: Additional keyword arguments passed by the signal handler.

    The function calls the `update_total()` method of the associated `Order`
    instance to recalculate the order totals based on the updated line items
    after deletion.
    """
    instance.order.update_total()
