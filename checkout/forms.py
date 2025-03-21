from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    A form for capturing order details including customer information and
    delivery address.

    This form is used to collect the full name, email, phone number, and
    delivery information of a customer during the checkout process.

    **Meta:**
    - The form uses the `Order` model, and includes fields such as full name,
    email, phone number, delivery method, and address details.

    **Attributes:**
    - `full_name`: Customer's full name.
    - `email`: Customer's email address.
    - `phone_number`: Customer's phone number.
    - `delivery_method`: Method of pickup or delivery.
    - `street_address`: Customer's street address.
    - `town_or_city`: Customer's town or city.
    - `postcode`: Customer's postal code.
    - `country`: Customer's country.

    **Initialization:**
    - The `__init__` method customizes the form:
        - Adds placeholders for each field.
        - Removes auto-generated labels by setting them to `False`.
        - Sets the autofocus attribute on the "Full Name" field.
        - Sets default values for `town_or_city` and `country`.
        - Applies custom CSS classes.
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'delivery_method', 'street_address', 'town_or_city',
                  'postcode', 'country')

    def __init__(self, *args, **kwargs):
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

        # Set the autofocus attribute on the full name field.
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Set default values for 'town_or_city' and 'country'
        self.fields['town_or_city'].initial = 'Gothenburg'
        self.fields['country'].initial = 'SE'

        for field in self.fields:
            if field != 'delivery_method':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].label = False  # Remove labels

        self.fields['delivery_method'].widget.attrs['class'] = 'form-select'
