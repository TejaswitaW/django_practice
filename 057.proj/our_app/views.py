from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student
# Create your views here.
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)     
        if fm.is_valid():
            print(fm.cleaned_data)
            print("Form Validated")
            name = fm.cleaned_data['name']             
            email = fm.cleaned_data['email']              
            pwd = fm.cleaned_data['password']              
            # print("Comment: ",fm.cleaned_data['comment'])  
            std = Student(name=name,email=email,password=pwd)
            std.save()       
            """
            for delete,
            std = Student(id=1)
            std.delete()
            """      
    else: 
        fm = StudentRegistration() 
    return render(request,'our_app/userreg_hidden.html',{'form':fm})
