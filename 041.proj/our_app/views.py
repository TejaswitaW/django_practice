from django.shortcuts import render
from .models import Student
# Create your views here.

def studinfo(request):
    stud = Student.objects.all()
    print("Queryset: ",stud)
    return render(request,'our_app/studetails.html',{'students':stud})
