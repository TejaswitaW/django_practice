from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Student

# Create your views here.
class StudentDetailView(DetailView):  
    model = Student 
    template_name = 'school/student.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['all_students'] = self.model.objects.all()
        return context


class StudentListView(ListView):
    model = Student


