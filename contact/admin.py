from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Customizes the Django admin interface for the Contact model.
    """
    list_display = ('message', 'read', )