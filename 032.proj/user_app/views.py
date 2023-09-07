from django.shortcuts import render

# Create your views here.
def user_welcome(request):
    return render(request,"user_app/user.html")