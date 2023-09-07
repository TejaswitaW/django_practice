from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Password(again)',widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data['password']
        rpwd = cleaned_data['rpassword']
        if pwd != rpwd:
            raise forms.ValidationError("Email or Password is Wrong")
   