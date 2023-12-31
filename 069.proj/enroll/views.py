from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User,Group
from .forms import SignUpForm,EditUserProfileForm,EditAdminProfileForm

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Your Account Created Successfully')
            user = fm.save()
            group = Group.objects.get(name='Editor')
            user.groups.add(group)           
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
                return HttpResponseRedirect('/dashboard/')
        else:        
            fm = AuthenticationForm()      
        return render(request,'enroll/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')
def user_dashboard(request):
    if request.user.is_authenticated:
      return render(request,'enroll/dashboard.html',{'name':request.user.username})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

