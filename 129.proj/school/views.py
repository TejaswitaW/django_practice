from django.views.generic.base import TemplateView
from django.views.generic import CreateView,UpdateView,DeleteView
from django import forms
from .models import Student
from .forms import StudentForm

# Create your views here.
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanksupdate'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/afterdelete'

      
class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class ThanksUpdateTemplateView(TemplateView):
    template_name = 'school/update_thanks.html'
    
class DeleteTemplateView(TemplateView):
    template_name = 'school/delete.html'
    

    
    


