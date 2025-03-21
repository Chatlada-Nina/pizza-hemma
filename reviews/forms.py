from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    A form for submitting a review.

    This form is based on the Review model and allows users to submit
    reviews with a body, rating, and optional image.

    **Fields:**
    - 'body': The content of the review (text).
    - 'rating': The rating given for the review (numeric).
    - 'image': An optional image associated with the review.

    **Meta:**
    The form is tied to the `Review` model and includes the fields 'body',
    'rating' and 'image' for the user to fill out when submitting a review.

    **Usage:**
    This form can be used in views for creating or updating review objects.
    """
    class Meta:
        model = Review
        fields = ('body', 'rating', 'image',)
