from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.

def thankyou(request):
    return render(request,'our_app/success.html')

def showformdata(request):
    if request.method == 'POST':
        #print(request.body)#b'csrfmiddlewaretoken=Xw3WUZGHy73qmBpWBpWiptXoj5xArZRCSVCd6jXZz0iVAoAEATQOsuqL5F0zie7v&name=Tejaswita&email=admin%40gmail.com'
        # print("Request Post: ",request.POST)
        fm = StudentRegistration(request.POST)
        # print(fm)
        
        if fm.is_valid():
            print(fm.cleaned_data)
            print("Form Validated")
            print("Name: ",fm.cleaned_data['name'])
            print("Email: ",fm.cleaned_data['email'])
            print("Password: ",fm.cleaned_data['password'])     
            # nm = fm.cleaned_data['name']  
            # return render(request,'our_app/success.html',{'name':nm})
            return HttpResponseRedirect('/user/success/')
        

    else: 
        fm = StudentRegistration() 
    return render(request,'our_app/userreg_hidden.html',{'form':fm})
