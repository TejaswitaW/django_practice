from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Student

# Create your views here.
class StudentDetailView(DetailView):
    # it expects single object,not list of objects
    model = Student #Students.objects.all()
    # we can give custom template name
    # now we have to use this template only
    template_name = 'school/student.html'
    # changing default context name(student)
    context_object_name = 'stu'
    pk_url_kwarg = 'id'

