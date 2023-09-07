from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,
                                primary_key=True) 
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()
"""
class Like(Page):
    '''this will create default one to one relationship with page_ptr_id coulmn'''
    likes = models.IntegerField()
"""

class Like(Page):
    '''Overrdiing default one to one relationship'''
    newpage = models.OneToOneField(Page,on_delete=models.CASCADE,
                                primary_key=True,parent_link=True) 
    likes = models.IntegerField()
