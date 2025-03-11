from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated labels and set autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_email': 'Email Address',
            'default_phone_number': 'Phone Number',
            'default_address': 'Your Address',
            'default_postcode': 'Postcode',
        }

        # Set the autofocus attribute on the full name field so the cursor start in the fullname field.
        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields: # iterate through forms fields adding star to placeholder if it's a required field on the model
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder # Set value in the dictionary placeholder for all placeholder attributes.
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False # Remove label fields since given placeholder are set.