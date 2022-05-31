from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'room_no', 'student_count', 'class_teacher']