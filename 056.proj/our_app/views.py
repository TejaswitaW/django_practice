from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)     
        if fm.is_valid():
            print(fm.cleaned_data)
            print("Form Validated")
            print("Name: ",fm.cleaned_data['name'])               
            print("Email: ",fm.cleaned_data['email'])               
            print("Password: ",fm.cleaned_data['password'])               
            # print("Comment: ",fm.cleaned_data['comment'])               
    else: 
        fm = StudentRegistration() 
    return render(request,'our_app/userreg_hidden.html',{'form':fm})
