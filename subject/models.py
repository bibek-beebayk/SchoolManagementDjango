from django.db import models
from teacher.models import Teacher
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=256, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    
    def __str__(self) -> str:
        return self.name

