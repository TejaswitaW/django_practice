from django.shortcuts import render
from .models import Student
from django.views.generic.list import ListView
# Create your views here.
class StudentListView(ListView):
    model = Student
    # default or custom any template name
    # you can keep,if custom there it will
    # be used else default use
    template_name = 'school/student.html'
    template_name_suffix = '_list'
    ordering = ['name']
    context_object_name = 'students'