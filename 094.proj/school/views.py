from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    '''
    student_data = Student.objects.all()
    print(student_data)
    '''
    '''
    student_data = Student.objects.filter(name__exact="Kush")
    '''
    '''
    student_data = Student.objects.filter(name__iexact="kush")
    '''
    '''
    student_data = Student.objects.filter(name__contains="u")
    '''
    '''
    student_data = Student.objects.filter(name__icontains="U")
    '''
    '''
    student_data = Student.objects.filter(id__in=[1,2])
    '''
    '''
    student_data = Student.objects.filter(marks__in=[95,99])
    '''
    '''
    student_data = Student.objects.filter(marks__gt=80)
    '''

    '''
    student_data = Student.objects.filter(marks__gte=80)
    '''
    '''student_data = Student.objects.filter(name__startswith='k')'''
    '''
    student_data = Student.objects.filter(name__endswith='h')
    '''
    '''     
    student_data = Student.objects.filter(marks__range=(80,96))
    '''
    '''
    student_data = Student.objects.filter(passdate__range=('2023-08-01','2023-08-12'))
    '''
    '''
    student_data = Student.objects.filter(passdate__range=('2023-08-01','2023-08-12'))
    '''
    '''
    student_data = Student.objects.filter(passdate__year=2023)
    '''
    '''
    student_data = Student.objects.filter(passdate__year__gt=2023)
    '''
    student_data = Student.objects.filter(passdate__year__gt=2023)
    print(student_data)

    return render(request,'school/home.html',{'students':student_data})
