from django import forms
from .models import MenuItem


class MenuForm(forms.ModelForm):
    """
    Form for creating and updating MenuItem instances.

    This form is used in the Django admin panel and other views
    to manage menu items. It applies Bootstrap styling to all fields.

    Attributes:
        Meta:
            model (MenuItem): The model associated with this form.
            fields (str): Specifies that all model fields should be included in
            the form.

    Methods:
        __init__: Customizes form field widgets to include Bootstrap classes.
    """

    class Meta:
        model = MenuItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
