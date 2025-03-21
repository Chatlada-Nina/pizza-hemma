from django.contrib import admin
from .models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Customizes the Django admin interface for the Contact model.

    Display fields in the contact model, including:
     - 'message'
     - 'read'
    Attributes:
        list_display(tuple): Fields to display in the admin list view.
    """
    list_display = ('message', 'read', )
