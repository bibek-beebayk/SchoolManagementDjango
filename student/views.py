from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from .models import Student
from .forms import StudentForm


# Create your views here.

class StudentView(View):

    greeting = 'Hello There! Welcome.'
    def get(self, request):
        # view logic
        students = Student.objects.all()
        context = {'students':students, 'greeting': self.greeting}
        return render(request, 'index.html', context)

    

def add_student(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')


    context = {'form':form}
    return render(request, 'student/add-student.html', context)

def show_students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student/all-students.html', context)


def student_details(request, id):
    student = Student.objects.get(id=id)

    context = {'student':student}
    return render(request, 'student/student-details.html', context)
