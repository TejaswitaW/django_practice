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

    
class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class ThanksUpdateTemplateView(TemplateView):
    template_name = 'school/update_thanks.html'
    
class StudentUpdateView(UpdateView):
    # which model,field you want to update
    model = Student
    fields = ['name','email','password']
    success_url = '/thanksupdate'




