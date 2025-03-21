from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    A form to handle user profile information, including fields:
    full name, email, phone number, address, and country.

    This form allows users to update their profile information, excluding
    the `user` field, which is handled automatically.

    **Meta:**
    - `model`: The form is based on the `UserProfile` model.
    - `exclude`: The `user` field is excluded from the form to avoid manual
    entry and is handled internally.

    **Customizations:**
    - Placeholder Text: The fields have customized placeholders for better UX.
    - Required Fields: A star is added to the placeholder text for fields
    marked as required.
    - Class and Autofocus: Each form field is given a `profile-form-input`
    CSS class and autofocus is set on the `default_full_name` field to improve
    the user experience.
    - Labels: The labels for fields are removed in favor of the placeholders,
    keeping the form clean.

    **Methods:**
    - `__init__(self, *args, **kwargs)`: Custom initialization to add
    placeholders, set autofocus on the full name field and configure
    other UI aspects like required fields and CSS classes.
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated labels and set
        autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_street_address': 'Your Address',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Postcode',
            'default_country': 'Country',
        }

        # Set the autofocus attribute on the full name field
        self.fields['default_full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
