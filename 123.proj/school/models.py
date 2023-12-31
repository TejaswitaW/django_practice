from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=70)

    # def get_absolute_url(self):
    #     return reverse('thanks')
    # after creation of student object redirect to this
    def get_absolute_url(self):
        return reverse('studetail',kwargs={'pk':self.pk})