from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Customize the django admin interface for the About model
    """
    summernote_fields = ('content',)
