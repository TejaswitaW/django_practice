from django.contrib import admin
from .models import Student
# Register your models here.
"""
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuid','stuname','stuemail')

admin.site.register(Student,StudentAdmin)
"""
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuid','stuname','stuemail')
