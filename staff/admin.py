from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'middle_name', 'last_name', 'job_designation', 'joining_date', 'salary']





@admin.register(models.StaffDepartment)
class StaffDepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'staff', 'department', 'job_description']

