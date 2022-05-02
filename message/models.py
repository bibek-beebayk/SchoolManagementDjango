from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='sender')
    receiver = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='receiver')
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=256)
    body = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

    
