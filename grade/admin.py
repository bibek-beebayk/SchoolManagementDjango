from django.contrib import admin
from . import models
# Register your models here.


class GradeSubjectInline(admin.TabularInline):
    model = models.GradeSubject
    extra = 1

@admin.register(models.Grade)
class GradeAdmin(admin.ModelAdmin):
    inlines = [GradeSubjectInline]
    list_display = ['id', 'name', 'room_no', 'student_count', 'class_teacher']