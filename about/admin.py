from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Customize the django admin interface for the About model.

    This class customizes the admin interface for the about model by using the
    summernote editor for the content field.

    Attributes:
    summernote_fields (tuple): Fields that should use the summernote richtext
    editor which is the 'content' field.
    """
    summernote_fields = ('content',)
