from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from grade.models import Grade

# Create your models here.
GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

class Student(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    grade = models.ForeignKey(
        Grade, on_delete=models.PROTECT, null=True)
    roll_no = models.PositiveSmallIntegerField()
    admission_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    previous_school = models.CharField(
        max_length=256, null=True, blank=True, verbose_name='Previous School (if any)')
    guardian_name = models.CharField(
        max_length=256, verbose_name="Guardian's Name", blank=True, null=True)
    guardian_profession = models.CharField(
        max_length=256, verbose_name="Guardian's Profession", blank=True, null=True)
    guardian_address = models.CharField(
        max_length=256, verbose_name="Guardian's Address", blank=True, null=True)
    guardian_phone = models.CharField(
        max_length=10, verbose_name="Guardian's Phone Number", blank=True, null=True)
    is_specially_abled = models.BooleanField(
        default=False, verbose_name="Is the student specially abled?", null=True)



    def __str__(self) -> str:
        return self.name

    class Meta:
        unique_together = ['grade', 'roll_no']


@receiver(signals.post_save, sender=Student)
def student_post_save(sender, instance, *args, **kwargs):
    print(instance.name + ' was successfully created.')
    # post_save logic goes here 