from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print("This is home view")
    return HttpResponse("Hello Home")