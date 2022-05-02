from django.contrib import admin
from . import models

# Register your models here.

class SingleSubjectInline(admin.TabularInline):
    model = models.SingleExam
    extra = 1

@admin.register(models.Exam)
class ExamAdmin(admin.ModelAdmin):
    inlines = [SingleSubjectInline]
    list_display = ['grade', 'start_date', 'end_date']

@admin.register(models.SingleExam)
class SingleExamAdmin(admin.ModelAdmin):
    pass





