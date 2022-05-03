from django.contrib import admin
from .models import Message

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'receiver', 'message_subject', 'created_at']
    list_filter = ['created_at', 'sender']
    search_fields = ['message_subject', 'sender__username', 'receiver__username']