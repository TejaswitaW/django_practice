from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'product_app/home.html')

def about(request):
    return render(request,'product_app/about.html')
    
def course(request):
    return render(request,'product_app/course.html')

