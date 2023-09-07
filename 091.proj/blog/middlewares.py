from typing import Any
from django.shortcuts import HttpResponse

class MyProcessMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        response = self.get_response(request)
        return response
    # if foll. return http response it doesnt call view
    # if return None,it will call view
    def process_view(request,*args,**kwargs):
        # return HttpResponse("This is before view")
        print("This is process view before view")
        return
    
class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        response = self.get_response(request)
        return response
    def process_exception(self,request,exception): 
        print("Exception Occured")
        msg = exception
        return HttpResponse(msg)
    
class MyTemplateResponseMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        response = self.get_response(request)
        return response
    def process_template_response(self,request,response): 
        print("Process Template Response From Middleware")
        response.context_data['name'] = 'Teju'
        return response