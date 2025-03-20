from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'delivery_method', 'street_address','town_or_city', 'postcode', 'country')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated labels and set autofocus on first field.
        """
        # Call the default init method to set the form up by default
        super().__init__(*args, **kwargs)

        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address': 'Your Address',
            'town_or_city': 'Town or City',
            'postcode': 'Postcode',
            'country': 'Country',
        }

        # Set the autofocus attribute on the full name field so the cursor starts in the full name field.
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Set default values for 'town_or_city' and 'country'
        self.fields['town_or_city'].initial = 'Gothenburg'
        self.fields['country'].initial = 'SE'

        for field in self.fields:  # Iterate through form fields, adding a star to the placeholder if it's a required field on the model
            if field != 'delivery_method':  # Skip adding placeholder for delivery_method
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            
            # self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False  # Remove labels

        self.fields['delivery_method'].widget.attrs['class'] = 'form-select'
       