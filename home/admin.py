from django.contrib import admin
from .models import SubscribedUsers


class SubscribedUsersAdmin(admin.ModelAdmin):
    """
    Admin interface customization for the SubscribedUsers model.

    This class customizes the display options for the SubscribedUsers model
    within the Django admin panel.

    **List Display:**
    - email: The email address of the subscribed user.
    - created_on: The timestamp when the subscription was created.
    """
    list_display = ("email", "created_on", )


admin.site.register(SubscribedUsers, SubscribedUsersAdmin)
