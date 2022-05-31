from django.db import models
from django.contrib.auth.models import User
from subject.models import Subject
from teacher.models import Teacher
from grade.models import Grade
from ckeditor.fields import RichTextField
from django_quill.fields import QuillField

# Create your models here.

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT, default=None)
    short_title = models.CharField(
        max_length=256, null=True, verbose_name="Short Title")
    description = QuillField(null=True, blank=True)
    submission_date = models.DateField(verbose_name="Submission Due Date")
    is_active = models.BooleanField(default=True)
    posted_by = models.ForeignKey(User, on_delete=models.PROTECT,null=True)
    # students = models.ManyToManyField(Student, through='AssignmentStudent')
    # attachments =

    def __str__(self) -> str: 
        return self.short_title
