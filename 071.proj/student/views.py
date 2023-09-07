from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response = render(request,'student/setcookie.html')
    response.set_signed_cookie('name','kush',salt='nm')
    #print(response)
    return response

def getcookie(request):
    name = request.get_signed_cookie('name',salt='nm')
    return render(request,'student/getcookie.html',{'name':name})

def delcookie(request):
    response = render(request,'student/delcookie.html')
    response.delete_cookie('name')
    return response