from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'vendor/home.html')
def info(request):
    return render(request,'vendor/vendor.html')
