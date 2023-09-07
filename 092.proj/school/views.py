from django.shortcuts import render
from .models import Student,Teacher
# Create your views here.

def home(request):
    """students = Student.objects.all()
    # query property gives sql query ran
    print(students.query)"""

    """students =  Student.objects.filter(marks=99)
    print(students)
    print(students.query)"""

    '''students =  Student.objects.exclude(marks=99)
    print(students)
    print(students.query)'''

    '''students =  Student.objects.order_by('-name')
    print(students)
    print(students.query)'''

    '''students =  Student.objects.order_by('?')
    print(students)
    print(students.query)'''

    '''# students =  Student.objects.order_by('name').reverse()
    # we get last 2
    students =  Student.objects.order_by('name').reverse()[:2]
    print(students)
    print(students.query)'''

    '''students =  Student.objects.values('name','city')
    print(students)
    print(students.query)'''

    '''students =  Student.objects.distinct('name')
    print(students)
    print(students.query)'''

    '''
    students =  Student.objects.values_list('name', 'marks','city',named=True)
    print(students)
    print(students.query)'''

    '''
    students =  Student.objects.dates('pass_date','year')
    print(students)
    print(students.query)'''
    qs1 = Student.objects.values_list('id','name',named=True)
    qs2 = Teacher.objects.values_list('id','name',named=True)

    students =  qs2.union(qs1)
    print(students)
    print(students.query)
    return render(request,'school/home.html',{'students':students})