from django.shortcuts import render
from .models import Student
from django.db.models import Q


# Create your views here.

def home(request):
    '''
    students_data = Student.objects.filter(Q(id=1)&Q(marks=99))
    '''   
    '''
    students_data = Student.objects.filter(Q(id=1)|Q(marks=95)) 
    '''  
    students_data = Student.objects.filter(~Q(id=3))   
    return render(request,'school/home.html',{'students':students_data})
