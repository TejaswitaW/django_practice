from typing import List
from django.shortcuts import render
from .models import Student
from django.views.generic.list import ListView
# Create your views here.
class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'school/student_list.html'
    # filter data
    def get_queryset(self):
        return Student.objects.filter(course='CS')
    
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context
    
    def get_template_names(self):
        if self.request.COOKIES['user'] == 'ram':
            template_name = 'school/ram.html'
        else:
            template_name = self.template_name
            #print("temp: ",template_name)
        return [template_name]