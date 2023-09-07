from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from .forms import SignUpForm,EditUserProfileForm,EditAdminProfileForm

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
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST,instance=request.user)
                users = User.objects.all()
            else:
                users = None
                fm = EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                messages.success(request,'Your Profile Updated Successfully')
                fm.save()
        else: 
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                users = None
                fm = EditUserProfileForm(instance=request.user)
        return render(request,'enroll/profile.html',{'name':request.user.username,'form':fm,'users':users})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# user change password with old password
def user_change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(request.user,data=request.POST)
            # print(fm)
            if fm.is_valid():
                fm.save()
                # for updating session
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(request.user)
        return render(request,'enroll/changepass.html',{'form':fm})
    else:
         return HttpResponseRedirect('/login/')
    
def user_detail(request,id):
    if request.user.is_authenticated:
        user = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=user)
        return render(request,'enroll/userdetail.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')


    