from django.db import models
from subject.models import Subject
from grade.models import Grade

# Create your models here.

class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT, null=True, related_name='exam')
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField( null=True)
    full_marks = models.PositiveSmallIntegerField()
    pass_marks = models.PositiveSmallIntegerField()
    room_no = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
