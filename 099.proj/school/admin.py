from django.contrib import admin
from .models import Student,ExamCenter

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city','name','roll']

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id','cname','city']


