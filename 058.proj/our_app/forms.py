from django import forms
from django.core import validators
from .models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','password']

    
    
   