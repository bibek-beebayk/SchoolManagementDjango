
import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from pytz import timezone
# Create your models here.

class Teacher(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

    name = models.CharField(max_length=256)
    mobile_number = models.CharField(max_length=10)
    address = models.CharField(max_length=256)
    email = models.EmailField(blank=True, null=True)
    joined_on = models.DateField(blank=True, default=datetime.date.today(), null=True )
    salary = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    specialization = models.CharField(max_length=256)
    proficient_subjects = ArrayField(models.CharField(max_length=256 ), default=list)
    dob = models.DateField(verbose_name='Date of Birth', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name + '->' + self.specialization
