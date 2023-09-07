from django.shortcuts import render
from .models import Student,Teacher
# Create your views here.

def home(request):
    # student = Student.objects.get(pk=1)
    # student = Student.objects.first()
    # student = Student.objects.last()
    # student = Student.objects.latest('pass_date')
    # students = Student.objects.all()
    # print(students.exists())
    # print(student.query)
    ''' s = Student.objects.get_or_create(name='TK',roll=111,city='Bang',marks=99,pass_date='2019-03-19')
    print(s[0])
    print(s[1])'''
    '''
    s = Student.objects.filter(id=1).update(name="Golu")
    s = Student.objects.filter(id=2).update(name="Goli")
    '''
    '''student_data,created = Student.objects.update_or_create(id=14,name='Sameer',defaults={'name':'Kohli'})
    print(student_data)
    print(created)'''

    '''
    all_student_data = Student.objects.all()
    for student in all_student_data:
        student.city = "Bhel"
    student_data = Student.objects.bulk_update(all_student_data,['city'])'''

    ''' student_data = Student.objects.in_bulk([1,2])
    print(student_data[1].name)
    print(student_data[2].name)'''

    '''
    student_data = Student.objects.in_bulk([])
    print(student_data)# blank dictionary
    '''
    '''
    student_data = Student.objects.in_bulk()
    print(student_data)
    '''
    '''student_data = Student.objects.get(pk=14)
    deleted = student_data.delete()'''

    '''student_data = Student.objects.filter(marks=95).delete()
    print(student_data)'''

    '''student_data = Student.objects.filter(marks=95).delete()
    print(student_data)'''

    '''
    student_data = Student.objects.all().delete()
    print(student_data)'''
    
    teacher_data = Teacher.objects.all()
    print(teacher_data.count())
    return render(request,'school/home.html')