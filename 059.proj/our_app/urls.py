from django.urls import path
from . import views

urlpatterns = [
    path('<int:my_id>/', views.show,{'check':"Ok"},name='user'),
    path('<int:my_id>/<int:my_subid>/', views.show_subdetails,name='subdetail'),
    path('home/',views.home,name='home')
]