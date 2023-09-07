from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

# def home(request):
#     mv = cache.get('movie','has_expired')
#     if mv == 'has_expired':
#         cache.set('movie','TAK',30)
#         mv = cache.get('movie')
#     return render(request,'enroll/course.html',{'fm':mv})

# def home(request):
#     mv = cache.get_or_set('fees',6000,30,version=2)
#     return render(request,'enroll/course.html',{'fm':mv})

# def home(request):
#     data = {'name':'Kush','roll':150}
#     cache.set_many(data,30)
#     sv = cache.get_many(data)
#     return render(request,'enroll/course.html',{'fm':sv})

# def home(request):
#     cache.delete('fees',version=2)
#     return render(request,'enroll/course.html')

# def home(request):
#     cache.set('roll',101,600)
#     rv = cache.get('roll')
#     return render(request,'enroll/course.html',{'fm':rv})

# def home(request):
#     rv = cache.decr('roll',delta=1)
#     return render(request,'enroll/course.html',{'fm':rv})

def home(request):
    cache.clear()
    return render(request,'enroll/course.html')