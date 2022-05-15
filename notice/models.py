from django.db import models
from ckeditor.fields import RichTextField
from  django.contrib.auth.models import User

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=256)
    description = RichTextField()
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
