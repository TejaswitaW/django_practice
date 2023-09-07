from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print("This is home view")
    # a = 10/0
    return HttpResponse("Hello Home")

def excp(request):
    print("This is home view")
    a = 10/0
    return HttpResponse("Hello Exception")

def user_info(request):
    print("This is user info view")
    context = {'name':'Kush'}
    return TemplateResponse(request,'blog/user.html',context)