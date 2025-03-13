from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number','delivery_method', 'address', 'postcode',)

def __init__(self, *args, **kwargs):
    """
    Add placeholders and classes, remove auto-generated labels and set autofocus on first field.
    """
    # Call the default init method to set the form up by default
    super().__init__(*args, **kwargs)
    placeholders = {
        'full_name': 'Full Name',
        'email':'Email Address',
        'phone_number':'Phone Number',
        'address':'Your Address',
        'postcode':'Postcode',
    }

    # Set the autofocus attribute on the full name field so the cursor start in the fullname field.
    self.fields['full_name'].widget.attrs['autofocus'] = True
    for field in self.fields: # iterate through forms fields adding star to placeholder if it's a required field on the model
        if self.fields[field].required:
            placeholder = f'{placeholders[field]} *'
        else:
            placeholder = placeholders[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder # Set value in the dictionary placeholder for all placeholder attributes.
        self.fields[field].widget.attrs['class'] = 'stripe-style-input' # Add CSS class
        self.fields[field].label = False # Remove label fields since given placeholder are set.