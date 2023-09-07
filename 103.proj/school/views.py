from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):  
    student_data = Student.objects.all()
    print(student_data)
    return render(request,'school/home.html',{'students':student_data})

def order_name(request):  
    student_data = Student.students.all()
    print(student_data)
    return render(request,'school/home.html',{'students':student_data})

def roll_range(request):  
    student_data = Student.students.get_stu_roll_range(101,103)
    print(student_data)
    return render(request,'school/home.html',{'students':student_data})
