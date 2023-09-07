from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Kush'
    request.session['gname'] = 'Tej'
    return render(request,'student/setsession.html')

def getsession(request):
    name = request.session['name'] 
    gname = request.session['gname'] 
    return render(request,'student/getsession.html',{'name':name,'gname':gname})

def delsession(request):
    del request.session['name'] 
    return render(request,'student/delsession.html')