from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
def myview(request):
    return HttpResponse("<h1>Function Based View</h1>")

# class MyView(View):
#     def get(self,request):
#         return HttpResponse("<h1>Class Based View</h1>")
    
# class MyView(View):
#     name = "Kush"
#     def get(self,request):
#         return HttpResponse(f"<h1>{self.name}</h1>")
    
class MyView(View):
    name = "Kush"
    def get(self,request):
        return HttpResponse(f"<h1>{self.name}</h1>")
    
class MyViewChild(MyView):
    def get(self,request):
        return HttpResponse(f"<h1>{self.name}</h1>")