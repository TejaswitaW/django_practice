# def page_middleware(get_response):
#     print("One Time Initialization")
#     def my_function(request):
#         print("This is before view")
#         response = get_response(request)
#         print("This is after view")
#         return response
#     return my_function
from django.shortcuts import render,HttpResponse

class PageMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Page Initialization")
    def __call__(self,request):
        print("This is Page before view")
        response = self.get_response(request)
        print("This is Page after view")
        return response
    
class AccountMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Account Initialization")
    def __call__(self,request):
        print("This is Account before view")
        # it does not go to view and next middleware also
        response = HttpResponse("Return,Dont go futher")
        print("This is Account after view")
        return response
    
class UserMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time User Initialization")
    def __call__(self,request):
        print("This is User before view")
        response = self.get_response(request)
        print("This is User after view")
        return response
