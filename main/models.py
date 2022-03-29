from email.policy import default
from django.db import models


GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
# Create your models here.


class Teacher(models.Model):

    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(
        max_length=56, blank=True, null=True)
    last_name = models.CharField(max_length=256)
    mobile_number = models.CharField(max_length=10)
    address = models.CharField(max_length=256)
    email = models.EmailField()
    joining_date = models.DateField()
    salary = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    specialization = models.CharField(max_length=256)
    dob = models.DateField(verbose_name='Date of Birth')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        if self.middle_name:
            return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
        else:
            return self.first_name + ' ' + self.last_name


class Grade(models.Model):
    name = models.CharField(max_length=256)
    room_no = models.CharField(max_length=10)
    student_count = models.PositiveSmallIntegerField()
    class_teacher = models.OneToOneField(
        Teacher, on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self) -> str:
        return self.name

class GradeSubject(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    textbook = models.CharField(max_length=256, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, null=True)
    grade = models.ForeignKey('Grade', on_delete=models.PROTECT, related_name='+', null=True)

class Student(models.Model):
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(
        max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256)
    grade = models.ForeignKey(
        Grade, on_delete=models.PROTECT, null=True)
    roll_no = models.PositiveSmallIntegerField()
    admission_date = models.DateField()
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    previous_school = models.CharField(
        max_length=256, null=True, blank=True, verbose_name='Previous School (if any)')
    guardian_name = models.CharField(
        max_length=256, verbose_name="Guardian's Name")
    guardian_profession = models.CharField(
        max_length=256, verbose_name="Guardian's Profession")
    guardian_address = models.CharField(
        max_length=256, verbose_name="Guardian's Address")
    guardian_phone = models.CharField(
        max_length=10, verbose_name="Guardian's Phone Number")
    is_specially_abled = models.BooleanField(
        default=False, verbose_name="Is the student specially abled?", null=True)

    def __str__(self) -> str:
        if self.middle_name:
            return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
        else:
            return self.first_name + ' ' + self.last_name


class Department(models.Model):
    name = models.CharField(max_length=256, verbose_name="Department Name")

    def __str__(self) -> str:
        return self.name


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
    


class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT, default=None)
    short_title = models.CharField(
        max_length=256, null=True, verbose_name="Short Title")
    description = models.TextField(null=True, blank=True)
    submission_date = models.DateField(verbose_name="Submission Due Date")
    is_active = models.BooleanField(default=True)
    # students = models.ManyToManyField(Student, through='AssignmentStudent')
    # attachments =

    def __str__(self) -> str:
        return self.grade + ' ' + self.subject




class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT, null=True)
    exam_date = models.DateField(verbose_name="Date of Exam")
    start_time = models.TimeField(verbose_name="Starting Time")
    end_time = models.TimeField(verbose_name="Ending Time", null=True)
    full_marks = models.PositiveSmallIntegerField(verbose_name="Full Marks")
    pass_marks = models.PositiveSmallIntegerField(verbose_name="Pass Marks")
    room_no = models.CharField(max_length=256, verbose_name="Room Number")
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.grade + ' ' + self.subject


class Fee(models.Model):

    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)

    admission_fee = models.IntegerField(null=True, blank=True)
    monthly_fee = models.IntegerField(null=True)
    transportation_fee = models.IntegerField(null=True)
    other_fee = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)

    # def __str__(self):
    #     return self.student

class Mark(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    full_mark = models.PositiveSmallIntegerField(default=100)
    pass_mark = models.PositiveSmallIntegerField(default=40)
    obtained_mark = models.PositiveSmallIntegerField()
    result = models.ForeignKey('Result', on_delete=models.PROTECT, related_name='+')

    

class Result(models.Model):
    RESULT_CHOICES = [('P', 'Pass'), ('F', 'Fail')]
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    full_marks = models.IntegerField()
    pass_marks = models.FloatField()
    obtained_marks = models.IntegerField(null=True)
    percentage = models.PositiveSmallIntegerField()
    result = models.CharField(max_length=1, choices=RESULT_CHOICES)

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
