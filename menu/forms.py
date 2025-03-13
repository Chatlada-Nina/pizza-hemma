from django import forms
from .models import MenuItem, MenuList


class MenuForm(forms.ModelForm):

    class Meta:
        model = MenuItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'