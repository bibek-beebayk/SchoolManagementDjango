from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=256, verbose_name="Department Name")
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)


    def __str__(self) -> str:
        return self.name
