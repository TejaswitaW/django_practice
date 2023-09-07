from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def home(request):
   return render(request,'our_app/home.html')
   
def show(request,my_id,check):
    print(check)
    if my_id == 1:
        student = {'id':my_id,'name':"Ram"}
    if my_id == 2:
        student = {'id':my_id,'name':"Kush"}
    if my_id == 3:
        student = {'id':my_id,'name':"Teju"}

    return render(request,'our_app/show.html',student)
   
def show_subdetails(request,my_id,my_subid):
    if my_id == 1 and my_subid == 5:
        student = {'id':my_id,'name':"Ram",'info':'Subdetails'}
    if my_id == 2 and my_subid == 6:
        student = {'id':my_id,'name':"Kush",'info':'Subdetails'}
    if my_id == 3 and my_subid == 7:
        student = {'id':my_id,'name':"Teju",'info':'Subdetails'}

    return render(request,'our_app/show.html',student)
   
# def show(request,my_id):
#    print(my_id)
#    return render(request,'our_app/show.html',{'id':my_id})