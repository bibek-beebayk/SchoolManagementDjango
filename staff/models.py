from django.db import models
from department.models import Department
from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField

# Create your models here.

class Staff(models.Model):
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(
        max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    job_designation = models.CharField(
        max_length=256)
    salary = models.IntegerField()
    joining_date = models.DateField()
    department = models.ManyToManyField(
        Department, through='StaffDepartment')
    image = VersatileImageField()
    

    def __str__(self) -> str:
        if self.middle_name:
            return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
        else:
            return self.first_name + ' ' + self.last_name

class StaffDepartment(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    job_description = models.TextField()

    class Meta:
        unique_together = [['staff', 'department']]
    



#TODO through attribute in many to many relations

#     subject1 = models.ForeignKey(Subject, von_delete=models.SET_NULL, null=True, blank=True, related_name='+', verbose_name='Subject')
#     subject1_marks = models.PositiveSmallIntegerField(default=0, verbose_name='Marks')

#     subject2 = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name='+', verbose_name='Subject')
#     subject2_marks = models.PositiveSmallIntegerField(default=0, verbose_name='Marks')

#     subject3 = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name='+', verbose_name='Subject')
#     subject3_marks = models.PositiveSmallIntegerField(default=0, verbose_name='Marks')

#     subject4 = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name='+', verbose_name='Subject')
#     subject4_marks = models.PositiveSmallIntegerField(default=0, verbose_name='Marks')

#     subject5 = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name='+', verbose_name='Subject')
#     subject5_marks = models.PositiveSmallIntegerField(default=0, verbose_name='Marks')

#     subject6 = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name='+', verbose_name='Subject')
#     subject6_marks = models.PositiveSmallIntegerField(default=0, verbose_name='Marks')

#     subject7 = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name='+', verbose_name='Subject')
#     subject7_marks = models.PositiveSmallIntegerField(default=0, verbose_name='Marks')

#     subject8 = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name='+', verbose_name='Subject')
#     subject8_marks = models.PositiveSmallIntegerField(default=0, verbose_name='Marks')

#     def total_marks():
#         total = 0


# class Result(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.PROTECT)
#     # obtained_marks = models.ForeignKey('Marks', on_delete=models.PROTECT, related_name ='+')

# class Marks(models.Model):
#     subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
#     marks = models.PositiveSmallIntegerField()
#     result = models.ForeignKey(Result, on_delete=models.CASCADE, default=None)
