from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']