from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Student

# Create your views here.
class StudentDetailView(DetailView):
    # it expects single object,not list of objects
    model = Student #Students.objects.all()