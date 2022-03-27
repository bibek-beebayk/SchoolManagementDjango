from email.policy import default
from django.db import models


GENDER_CHOICES = [('M','Male'), ('F', 'Female'), ('O', 'Other')]   
# Create your models here.
class Teacher(models.Model): 
    
    first_name = models.CharField(max_length=256,verbose_name='First Name')
    middle_name = models.CharField(max_length=56, blank=True, null=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=256, verbose_name='Last Name')
    mobile_number = models.CharField(max_length=10)
    address = models.CharField(max_length=256)
    email = models.EmailField()
    joining_date = models.DateField(verbose_name='Joining Date')
    salary = models.IntegerField()
    gender = models.CharField(max_length=1, choices= GENDER_CHOICES )
    specialization = models.CharField(max_length=256)
    dob = models.DateField(verbose_name='Date of Birth')

    def __str__(self) -> str:
        if self.middle_name:
            return self.first_name +' '+ self.middle_name + ' ' + self.last_name
        else:
            return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'Teachers'
        verbose_name_plural = 'Teachers'



class Grade(models.Model): 
    name = models.CharField(max_length=256)
    room_no = models.CharField(max_length=10)
    student_count = models.IntegerField()
    class_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'Classes'
        verbose_name_plural = 'Classes'


class Subject(models.Model):
    name = models.CharField(max_length=256)
    subject_teacher = models.ManyToManyField(Teacher, verbose_name='Subject Teacher')
    text_book = models.CharField(max_length=256, null=True, verbose_name='Text Book')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Subjects'
        db_table = 'Subjects'


class Student(models.Model):
    first_name = models.CharField(max_length=256, verbose_name='First Name')
    middle_name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=256, verbose_name='Last Name')
    enrolled_class = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, verbose_name='Enrolled Class')
    roll_no = models.PositiveSmallIntegerField(verbose_name='Roll Number') 
    admission_date = models.DateField(verbose_name='Admission Date')
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.DateField(verbose_name='Date of Birth')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    previous_school = models.CharField(max_length=256, null=True, blank=True, verbose_name='Previous School (if any)')
    guardian_name = models.CharField(max_length=256, verbose_name="Guardian's Name")
    guardian_profession = models.CharField(max_length=256, verbose_name="Guardian's Profession")
    guardian_address = models.CharField(max_length=256, verbose_name="Guardian's Address")
    guardian_phone = models.CharField(max_length=10, verbose_name="Guardian's Phone Number")
    is_specially_abled = models.BooleanField(default=False, verbose_name="Is the student specially abled?", null=True)
    
    def __str__(self) -> str:
        if self.middle_name:
            return self.first_name +' '+ self.middle_name + ' ' + self.last_name
        else:
            return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'Students'
        verbose_name_plural = 'Students'

class Department(models.Model):
    name = models.CharField(max_length=256, verbose_name="Department Name")

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'Departments'
        verbose_name_plural = 'Departments'


class Staff(models.Model):
    first_name = models.CharField(max_length=256, verbose_name="First Name")
    middle_name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=256, verbose_name = "Last Namr")
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=10, verbose_name="Phone Number")
    email = models.EmailField()
    job_designation = models.CharField(max_length=256, verbose_name="Job Designation")
    salary = models.IntegerField()
    joining_date = models.DateField(verbose_name="Joining Date")
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, verbose_name="Department")

    def __str__(self) -> str:
        if self.middle_name:
            return self.first_name +' '+ self.middle_name + ' ' + self.last_name
        else:
            return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = 'Staffs'
        db_table = 'Staffs'


class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, default=None)
    short_title = models.CharField(max_length=256, null=True, verbose_name="Short Title")
    description = models.TextField(null=True, blank=True)
    submission_date = models.DateField(verbose_name = "Submission Due Date")
    is_active = models.BooleanField(default=True)
    # attachments = 

    def __str__(self) -> str:
        return self.grade + ' ' + self.subject

    class Meta:
        verbose_name_plural = 'Assignments'
        db_table = 'Assignments'

class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)
    exam_date = models.DateField(verbose_name="Date of Exam")
    start_time = models.TimeField(verbose_name="Starting Time")
    end_time = models.TimeField(verbose_name="Ending Time", null=True)
    full_marks = models.PositiveSmallIntegerField(verbose_name="Full Marks")
    pass_marks = models.PositiveSmallIntegerField(verbose_name="Pass Marks")
    room_no = models.CharField(max_length=256, verbose_name="Room Number")
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.grade + ' ' + self.subject

    class Meta:
        verbose_name_plural = 'Exams'
        db_table = 'Exams'

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=True)
    admission_fee = models.IntegerField(null=True, blank=True)
    monthly_fee = models.IntegerField(null=True)
    transportation_fee = models.IntegerField(null=True)
    other_fee = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)

    class Meta:
        db_table = 'Fees'
        verbose_name_plural = 'Fees'

    # def __str__(self):
    #     return self.student

class Result(models.Model):
    RESULT_CHOICES = [('P', 'Pass'), ('F', 'Fail')]
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    full_marks = models.IntegerField()
    pass_marks = models.IntegerField()
    obtained_marks = models.IntegerField(null=True)
    percentage = models.PositiveSmallIntegerField()
    result = models.CharField(max_length=1, choices=RESULT_CHOICES)

    class Meta:
        db_table = 'Results'
        verbose_name_plural = 'Results'

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

