from django.db import models
from student.models import Student
# Create your models here.

class Fee(models.Model):

    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)

    admission_fee = models.IntegerField(null=True, blank=True)
    monthly_fee = models.IntegerField(null=True)
    transportation_fee = models.IntegerField(null=True)
    other_fee = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)

    # def __str__(self):
    #     return self.student