from django.contrib import admin
from .models import Review

# Register your models here.
admin.site.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_on', 'rating', 'approved')
    list_filter = ('approved', 'created_on', 'rating')
    search_fields = ('author__username', 'body')
    # Add the image field here
    readonly_fields = ['image']
