from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import ContactForm

# Create your views here.
class ContactFormView(FormView):
    template_name = 'school/contact.html'
    # instantiating form class, creating object
    form_class = ContactForm
    success_url = '/thankyou/'
    initial = {'name':"Kush"}
    # want data in the form
    def form_valid(self, form):
        # this method redirects you to ,
        # get_success_url method
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        # print(super().form_valid(form))
        # return super().form_valid(form)
        return HttpResponse("Message Saved thank you")

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'