from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
    if request.method == 'POST':
        print(request.body)#b'csrfmiddlewaretoken=Xw3WUZGHy73qmBpWBpWiptXoj5xArZRCSVCd6jXZz0iVAoAEATQOsuqL5F0zie7v&name=Tejaswita&email=admin%40gmail.com'
        # print("Request Post: ",request.POST)
        fm = StudentRegistration(request.POST)
        # print(fm)
        
        if fm.is_valid():
            print(fm.cleaned_data)
            print("Form Validated")
            print("Name: ",fm.cleaned_data['name'])
            print("Email: ",fm.cleaned_data['email'])
            fm = StudentRegistration()
    else: 
        fm = StudentRegistration() 
    return render(request,'our_app/userreg_hidden.html',{'form':fm})
