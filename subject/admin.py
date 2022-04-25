from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id','name']
