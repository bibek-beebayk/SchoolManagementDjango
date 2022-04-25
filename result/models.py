from django.db import models
from subject.models import Subject
from student.models import Student

# Create your models here.

class Mark(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    full_mark = models.PositiveSmallIntegerField(default=100)
    pass_mark = models.PositiveSmallIntegerField(default=40)
    obtained_mark = models.PositiveSmallIntegerField(default=0)    
    # subject_result = property(remarks)
    
    result = models.ForeignKey('Result', on_delete=models.SET_NULL, related_name='mark', null=True)

    

class Result(models.Model):
    RESULT_CHOICES = [('P', 'Pass'), ('F', 'Fail')]

    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)
    full_marks = models.IntegerField()
    pass_marks = models.IntegerField()
    obtained_marks = models.IntegerField(default=0)
    def calculate_percentage(self):
        return((self.obtained_marks/self.full_marks)*100)

    percentage = property(calculate_percentage)
    result = models.CharField(max_length=1, choices=RESULT_CHOICES)
