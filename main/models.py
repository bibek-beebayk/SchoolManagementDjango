
from django.db import models


    
# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    joining_date = models.DateField()
    salary = models.IntegerField()
    gender = models.CharField(max_length=1, choices= [('M','Male'), ('F', 'Female'), ('O', 'Other')])
    specialization = models.CharField(max_length=50)
    dob = models.DateField()

    def __str__(self) -> str:
        if self.middle_name:
            return self.first_name +' '+ self.middle_name + ' ' + self.last_name
        else:
            return self.first_name + ' ' + self.last_name



class Class(models.Model): 
    name = models.CharField(max_length=50)
    room_no = models.CharField(max_length=10)
    student_count = models.IntegerField()
    class_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name



class Subject(models.Model):
    name = models.CharField(max_length=50)
    subject_teacher = models.ManyToManyField(Teacher)
    text_book = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20)
    enrolled_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    roll_no = models.IntegerField()
    admission_date = models.DateField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    previous_school = models.CharField(max_length=100, null=True, blank=True)
    guardian_name = models.CharField(max_length=50)
    guardian_profession = models.CharField(max_length=50)
    guardian_address = models.CharField(max_length=50)
    guardian_phone = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        if self.middle_name:
            return self.first_name +' '+ self.middle_name + ' ' + self.last_name
        else:
            return self.first_name + ' ' + self.last_name