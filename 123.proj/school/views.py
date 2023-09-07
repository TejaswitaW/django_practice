from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from .models import Student

# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    fields = ['name','email','password']
    # success_url = '/thanks'

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'



class StudentDetailView(DetailView):
    model = Student


