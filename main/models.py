
from ast import Sub
from django.db import models


GENDER_CHOICES = [('M','Male'), ('F', 'Female'), ('O', 'Other')]   
# Create your models here.
class Teacher(models.Model):

    

    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=56, blank=True, null=True)
    last_name = models.CharField(max_length=256)
    mobile_number = models.CharField(max_length=10)
    address = models.CharField(max_length=256)
    email = models.EmailField()
    joining_date = models.DateField()
    salary = models.IntegerField()
    gender = models.CharField(max_length=1, choices= GENDER_CHOICES )
    specialization = models.CharField(max_length=256)
    dob = models.DateField()

    def __str__(self) -> str:
        if self.middle_name:
            return self.first_name +' '+ self.middle_name + ' ' + self.last_name
        else:
            return self.first_name + ' ' + self.last_name



class Class(models.Model): 
    name = models.CharField(max_length=256)
    room_no = models.CharField(max_length=10)
    student_count = models.IntegerField()
    class_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name



class Subject(models.Model):
    name = models.CharField(max_length=256)
    subject_teacher = models.ManyToManyField(Teacher)
    text_book = models.CharField(max_length=256, null=True)

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256)
    enrolled_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    roll_no = models.PositiveSmallIntegerField() 
    admission_date = models.DateField()
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    previous_school = models.CharField(max_length=256, null=True, blank=True)
    guardian_name = models.CharField(max_length=256)
    guardian_profession = models.CharField(max_length=256)
    guardian_address = models.CharField(max_length=256)
    guardian_phone = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        if self.middle_name:
            return self.first_name +' '+ self.middle_name + ' ' + self.last_name
        else:
            return self.first_name + ' ' + self.last_name


class Department(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name

class Staff(models.Model):
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    job_designation = models.CharField(max_length=256)
    salary = models.IntegerField()
    joining_date = models.DateField()
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        if self.middle_name:
            return self.first_name +' '+ self.middle_name + ' ' + self.last_name
        else:
            return self.first_name + ' ' + self.last_name


class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField()
    submission_date = models.DateField()
    # attachments = 