from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['id', 'grade', 'subject', 'exam_date', 'start_time', 'room_no']
