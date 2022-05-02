from django.db import models
# from student import models as student_models
from datetime import date
from django.utils import timezone

# Create your models here.

class Attendance(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.PROTECT, related_name='attendance_student')
    date = models.DateField(default=timezone.now)
    is_present = models.BooleanField(default=False)

    class Meta:
        unique_together = [['date', 'student']]

    def __str__(self):
        return (f'{self.date}  {self.student}  {self.is_present}')


