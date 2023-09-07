from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django import forms
from .models import Student

# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    fields = ['name','email','password']
    success_url = '/thanks'
    
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'myclass'})
        return form
    
class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'




