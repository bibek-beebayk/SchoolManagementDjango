from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    students = models.Student.objects.all()
    male_students = students.filter(gender='M')
    context = {'students':students, 'male_students':male_students}
    return render(request, 'index.html', context)