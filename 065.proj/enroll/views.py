from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:        
        fm = SignUpForm()
    return render(request,'enroll/signup.html',{'form':fm})

def user_login(request): 
    if not request.user.is_authenticated: 
        if request.method == 'POST': 
            fm = AuthenticationForm(request=request,data=request.POST) 
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user != None:
                    login(request,user)
                    messages.success(request,"Logged in Successfully")
                return HttpResponseRedirect('/profile/')
        else:        
            fm = AuthenticationForm()      
        return render(request,'enroll/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
def profile(request):
    # print(request)
    # print("Request: ",request.user.username)
    # print("Request: ",request.user.email)
    # print("Request: ",request.user.password)
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html',{'name':request.user.username})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
