from django.dispatch import Signal,receiver
# creating signal
notification = Signal(providing_args=['request','user'])

# receiver function
@receiver(notification)
def show_notification(sender,**kwargs):
    print(sender)
    print(kwargs)
    print(notification)