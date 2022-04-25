from django.contrib import admin
from . import models
from datetime import datetime
# Register your models here.

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade', 'phone', 'address', 'dob']

    # def age_in_years(self, student):
    #     return (datetime.date.today()-student.dob).days//365
    #     # return days.days//365