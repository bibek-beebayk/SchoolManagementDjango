from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=256, verbose_name="Department Name")

    def __str__(self) -> str:
        return self.name