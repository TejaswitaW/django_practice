from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'school/newhome.html'

class NewHomeView(TemplateView):
    template_name = 'school/newhomeview.html'
    def get_context_data(self, **kwargs):
        print("Kwargs: ",kwargs)
        context = super().get_context_data(**kwargs)
        print("Kwargs 1: ",context)
        context['name'] = 'Ram'
        context['city'] = 'Mumbai'
        return context
    
