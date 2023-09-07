from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django import forms
from .models import Student
from .forms import StudentForm

# Create your views here.
class StudentCreateView(CreateView):
    form_class = StudentForm
    # here we have to provide template as we are using form_class
    template_name = 'school/student_form.html'
    success_url = '/thanks'

    
class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'




