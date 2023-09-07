from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User

# reciever function
# @receiver(user_logged_in,sender=user)
def login_success(sender,request,user,**kwargs):
    print("----------------------------------")
    print("Logged-in Signal... Run Intro.. ")
    print("Sender: ",sender)
    print("Request: ",request)
    print("User: ",user)
    print("Kwargs: ",kwargs)

user_logged_in.connect(login_success,sender=User)

@receiver(user_logged_out,sender=User)
def logout_success(sender,request,user,**kwargs):
    print("----------------------------------")
    print("Logged-out Signal... Run Intro.. ")
    print("Sender: ",sender)
    print("Request: ",request)
    print("User: ",user)
    print("Kwargs: ",kwargs)

@receiver(user_login_failed)
def login_fialed(sender,credentials,request,**kwargs):
    print("----------------------------------")
    print("Logged-in failed Signal... Run Intro.. ")
    print("Sender: ",sender)
    print("Request: ",request)
    print("Credentials: ",credentials)
    print("Kwargs: ",kwargs)
