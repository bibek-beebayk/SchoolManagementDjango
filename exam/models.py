from django.db import models
from subject.models import Subject
from grade.models import Grade

# Create your models here.

class Exam(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT, null=True, related_name='exam')
    start_date = models.DateField()
    end_date = models.DateField()
    

class SingleExam(models.Model):
    date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT) 
    start_time = models.TimeField()
    end_time = models.TimeField()
    full_marks = models.PositiveSmallIntegerField(default=100)
    pass_marks = models.PositiveSmallIntegerField(default=40)
    # exam_room = models.CharField(max_length=256)
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT, default=None)

