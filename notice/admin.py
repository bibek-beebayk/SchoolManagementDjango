from django.contrib import admin
from . models import Notice

# Register your models here.

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'created_by']
    search_field = ['title', 'description']
    
