from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete, pre_migrate,post_migrate
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.backends.signals import connection_created
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

@receiver(pre_save,sender=User)
def at_begining_save(sender,instance,**kwargs):
    print("----------------------------------")
    print("Pre save Signal... Run Intro.. ")
    print("Sender: ",sender)
    print("Instance: ",instance)
    print("Kwargs: ",kwargs)

@receiver(post_save,sender=User)
def at_end_save(sender,instance,created,**kwargs):
    if created:
        print("----------------------------------")
        print("Post save Signal... Run Intro.. ")
        print("New record is getting created")
        print("Sender: ",sender)
        print("Instance: ",instance)
        print("Created: ",created)
        print("Kwargs: ",kwargs)
    else:
        print("----------------------------------")
        print("Post save Signal... Run Intro.. ")
        print("Record is getting updated")
        print("Sender: ",sender)
        print("Instance: ",instance)
        print("Created: ",created)
        print("Kwargs: ",kwargs)

@receiver(pre_delete,sender=User)
def at_begining_delete(sender,instance,**kwargs):
    print("----------------------------------")
    print("Pre Delete Signal... Run Intro.. ")
    print("Record is getting deleted")
    print("Sender: ",sender)
    print("Instance: ",instance)
    print("Kwargs: ",kwargs)

@receiver(post_delete,sender=User)
def at_end_delete(sender,instance,**kwargs):
    print("----------------------------------")
    print("Post Delete Signal... Run Intro.. ")
    print("Record is getting deleted")
    print("Sender: ",sender)
    print("Instance: ",instance)
    print("Kwargs: ",kwargs)

@receiver(pre_init,sender=User)
def at_begining_init(sender,*args,**kwargs):
    print("----------------------------------")
    print("Pre init Signal... Run Intro.. ")
    print("Sender: ",sender)
    print("Args: ",args)
    print("Kwargs: ",kwargs)

@receiver(post_init,sender=User)
def at_end_delete(sender,*args,**kwargs):
    print("----------------------------------")
    print("Post init Signal... Run Intro.. ")
    print("Sender: ",sender)
    print("Args: ",args)
    print("Kwargs: ",kwargs)

@receiver(request_started)
def at_request_Started(sender,environ,**kwargs):
    print("----------------------------------")
    print("Request Start...")
    print("Sender: ",sender)
    print("Environ: ",environ)
    print("Kwargs: ",kwargs)

@receiver(request_finished)
def at_request_finished(sender,**kwargs):
    print("----------------------------------")
    print("Request Finished...")
    print("Sender: ",sender)
    print("Kwargs: ",kwargs)

@receiver(got_request_exception)
def at_request_exception(sender,request,**kwargs):
    print("----------------------------------")
    print("Got Request Exception...")
    print("Sender: ",sender)
    print("Request: ",request)
    print("Kwargs: ",kwargs)


@receiver(pre_migrate)
def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("----------------------------------")
    print("At Migrate...")
    print("Sender: ",sender)
    print("app_config: ",app_config)
    print("verbosity: ",verbosity)
    print("interactive: ",interactive)
    print("using: ",using)
    print("plan: ",plan)
    print("apps: ",apps)

@receiver(post_migrate)
def at_end_migrate_flush(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("----------------------------------")
    print("At Post Migrate...")
    print("Sender: ",sender)
    print("app_config: ",app_config)
    print("verbosity: ",verbosity)
    print("interactive: ",interactive)
    print("using: ",using)
    print("plan: ",plan)
    print("apps: ",apps)

@receiver(connection_created)
def conn_db(sender,connection,**kwargs):
    print("----------------------------------")
    print("Initial connection to the database...")
    print("Sender: ",sender)
    print("Connection: ",connection)
    print("Kwargs: ",kwargs)

  

