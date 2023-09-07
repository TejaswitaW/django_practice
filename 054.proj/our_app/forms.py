from django import forms
from django.core import validators

def starts_s(value):
    if value[0].lower() != 's':
        raise forms.ValidationError("Name should start with s")


class StudentRegistration(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    name = forms.CharField(validators=[starts_s])
    email = forms.EmailField()