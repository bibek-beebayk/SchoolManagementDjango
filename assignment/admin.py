from django.contrib import admin
from . import models

# Register your models here.

admin.site.site_header = "MySchool"

@admin.register(models.Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'grade', 'short_title', 'submission_date']