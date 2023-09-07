from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    name = forms.CharField(error_messages={'required':'Enter Your Name'})
    email = forms.EmailField(error_messages={'required':'Enter Your Email'},min_length=5,max_length=10)
    password = forms.CharField(widget=forms.PasswordInput,
                               error_messages={'required':'Enter Your password'})
    
    
   