from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
# Create your views here.
   
class MyView(View):
    def get(self,request):
        return render(request,'school/home.html')
    
class AboutMyView(View):
    def get(self,request):
        context = {"name":"Ram"}
        return render(request,'school/about.html',context)
    
def contactform(request,template_name):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you for submission')
    else:
        form = ContactForm()
        return render(request,template_name,{'form':form})


class ContactClass(View):
     template_name = ''
     def get(self,request):
         form = ContactForm()
         return render(request,self.template_name,{'form':form})
     def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you for submission')