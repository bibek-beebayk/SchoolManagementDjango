from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_header = "MySchool"

@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'middle_name', 'last_name','gender', 'salary', 'specialization']

@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'room_no', 'student_count', 'class_teacher']


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text_book']


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name', 'enrolled_class', 'phone', 'address']