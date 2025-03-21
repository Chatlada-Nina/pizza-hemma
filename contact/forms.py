from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A form used to collect contact information, feedback, and inquiries from
    users.

    This form is linked to the `Contact` model and includes the fields:
    `name`, `email`, and `message`. It is intended for use in handling
    inquiries or feedback submissions from users.

    Attributes:
        name (forms.CharField): Field for the user's full name.
        email (forms.EmailField): Field for the user's email address.
        message (forms.CharField): Field for the user's message or feedback.
    """
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
