from django.urls import path
from . import views

urlpatterns = [
    path('userreg/', views.showformdata,name='userreg'),
]