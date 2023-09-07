from django.shortcuts import render
from .forms import StudentRegistration

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
            print(name)
            print(email)
            print(pwd)         
    else: 
        fm = StudentRegistration() 
    return render(request,'our_app/userreg_hidden.html',{'form':fm})
