from django.db import models
from teacher.models import Teacher
from subject.models import Subject

# Create your models here.

class Grade(models.Model):
    name = models.CharField(max_length=256, unique=True)
    room_no = models.CharField(max_length=10, null=True, blank=True)
    student_count = models.PositiveSmallIntegerField(null=True, blank=True)
    class_teacher = models.OneToOneField(
        Teacher, on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        unique_together = [['name', 'class_teacher']]   



