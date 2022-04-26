from django.db import models
from teacher.models import Teacher
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=256, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self) -> str:
        return self.name




# @receiver(post_save, sender=Subject)
# def subject_post_save(self, instance, *args, **kwargs):
#     self.created_by = self.