from django.urls import path
from . import views

urlpatterns = [
    path('userreg/', views.showformdata,name='userreg'),
    path('success/',views.thankyou,name='thankyou')
]