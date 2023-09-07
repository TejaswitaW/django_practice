from django.shortcuts import render
from .models import Student
from django.db.models import Avg,Sum,Min,Max,Count

# Create your views here.

def home(request):
    students_data = Student.objects.all()
    average = students_data.aggregate(Avg('marks'))
    sum = students_data.aggregate(Sum('marks'))
    min = students_data.aggregate(Min('marks'))
    max = students_data.aggregate(Max('marks'))
    count = students_data.aggregate(Count('marks'))
    print("Average: ",average)
    return render(request,'school/home.html',{'students':students_data,'average':average,
                                              'sum':sum,'min':min,'max':max,'count':count})
