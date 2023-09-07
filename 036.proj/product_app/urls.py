from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.home,name='homeurl'),
    path('about/',views.about,name='abouturl'),
    path('course/',views.course,name='courseurl')
]