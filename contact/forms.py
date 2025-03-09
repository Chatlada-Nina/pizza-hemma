from django import forms
from .models import Contact


# Create ContactForm that inherit from a built-in Django class.
# Use Meta to tell ModelForm what models and fields we want in our form.
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')