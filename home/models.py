from django.db import models

# Create your models here.


class SubscribedUsers(models.Model):
    """
    Represents a user who has subscribed to the platform.

    **Fields:**
    - email: The email address of the subscribed user (unique).
    - created_on: The date when the subscription was created.

    **Meta:**
    - verbose_name_plural: Specifies the plural name for the model in the admin
    interface.
    """

    class Meta:
        verbose_name_plural = 'Subscribed users'

    email = models.EmailField(unique=True, max_length=100)
    created_on = models.DateField(auto_now_add=True)

    # Display class object as a string to improve readable for admin
    def __str__(self):
        return self.email
