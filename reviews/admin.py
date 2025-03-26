from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Customizes the Django admin interface for the Review model.

    Attributes:
      - 'author' displays the author of the review.
      - 'created_on' shows when the review was created.
      - 'rating' shows the rating given in the review.
      - 'approved' shows whether the review is approved.

    - list_filter: Adds filtering options in the sidebar of the admin page.
      - Filters the list by 'approved' status, 'created_on' date, and 'rating'.

    - search_fields: Allows searching the reviews based on fields.
      - Allows searching by the author's username ('author__username')
      and the review body ('body').

    - readonly_fields: Marks the fields that cannot be edited in admin panel.
      - The 'image' field is marked to prevent editing in the admin view.

    **Usage:**
    This class is automatically used by Django's admin interface to manage
    review objects.
    """
    list_display = ('author', 'created_on', 'rating', 'approved')
    list_filter = ('approved', 'created_on', 'rating')
    search_fields = ('author__username', 'body')
    readonly_fields = ['image']


admin.site.register(Review)
