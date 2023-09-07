from django.shortcuts import render
# from .models import Student
from django.db.models import Q


# Create your views here.

def home(request):
    return render(request,'school/home.html')
