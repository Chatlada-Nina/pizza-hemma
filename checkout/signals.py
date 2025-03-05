from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineMenu

# Use the receiver decorator to tell that we received the post_save signals from the OrderLineMenu method.
@receiver(post_save, sender=OrderLineMenu)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update orderl total on linemenu update/create.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineMenu)
def update_on_delete(sender, instance, **kwargs):
    """
    Update orderl total on linemenu delete.
    """
    instance.order.update_total()