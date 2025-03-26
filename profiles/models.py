from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user profile model for maintaining default delivery information and
    order history.

    This model extends the default Django User model by providing additional
    fields for storing default contact information (e.g., full name, email,
    phone number, address, postcode, and country) to facilitate order and
    delivery processes.

    **Fields:**
    - `user`: A one-to-one relationship with the `User` model, linking each
    profile to a specific user.
    - `default_full_name`: The user's full name, used for delivery purposes.
    - `default_email`: The user's email address for order and delivery info.
    - `default_phone_number`: The user's phone number for contact purposes.
    - `default_street_address`: The user's default street address for delivery.
    - `default_town_or_city`: The town or city of the user's address.
    - `default_postcode`: The postcode of the user's address.
    - `default_country`: The country of the user's address.

    **Methods:**
    - `__str__(self)`: Returns the username associated with the user profile,
      improving readability in the admin interface.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=50, null=True, blank=True)
    default_email = models.EmailField(max_length=200, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    default_street_address = models.CharField(max_length=100, null=True,
                                              blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True,
                                            blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the UserProfile when a User instance is saved.

    This function is triggered automatically via the `post_save` signal
    whenever a new `User` is created or an existing `User` is updated.
    It ensures that a corresponding `UserProfile` is created or updated for
    each user.

    **Actions:**
    - If a new user is created, a `UserProfile` is created for the user.
    - If an existing user is updated, the associated `UserProfile` is saved.

    **Parameters:**
    - `sender`: The model class that sent the signal, in this case, `User`.
    - `instance`: The instance of the `User` model that was saved.
    - `created`: Boolean value indicating if the instance was created/updated.
    - `**kwargs`: Additional keyword arguments passed by the signal.
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: save the profile
    instance.userprofile.save()
