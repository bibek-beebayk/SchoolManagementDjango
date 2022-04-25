from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','gender', 'salary', 'specialization']