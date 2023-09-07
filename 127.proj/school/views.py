from django.views.generic.base import TemplateView
from django.views.generic import CreateView,UpdateView
from django import forms
from .models import Student
from .forms import StudentForm

# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    fields = ['name','email','password']
    success_url = '/thanks'

    def get_form(Self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'myclass'})
        return form
    
class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class ThanksUpdateTemplateView(TemplateView):
    template_name = 'school/update_thanks.html'
    
class StudentUpdateView(UpdateView):
    # which model,field you want to update
    model = Student
    fields = ['name','email','password']
    success_url = '/thanksupdate'
    
    def get_form(Self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'myclass'})
        return form




