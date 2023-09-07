from django.shortcuts import render
from django.contrib import messages
from .forms import StudentRegistration,TeacherRegistration

# Create your views here.
def stduent_form(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.add_message(request,messages.SUCCESS,"Your Account Successfully Created")
            messages.success(request,"Account Successfully Created")
    else:
        fm = StudentRegistration()
    return render(request,'our_app/student.html',{'form':fm})

def teacher_form(request):
    if request.method == 'POST':
        fm = TeacherRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            # messages.add_message(request,messages.SUCCESS,"Your Account Successfully Created")
            messages.success(request,"Account Successfully Created")
    else:
        fm = TeacherRegistration()
    return render(request,'our_app/student.html',{'form':fm})