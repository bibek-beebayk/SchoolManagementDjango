from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StudentView.as_view(), name='index'),
    path('all-students/', views.show_students, name='all-students'),
    path('add-student/', views.add_student, name='add-student'),
    path('student-details/<int:id>/', views.student_details, name='student-details'),
    # path('api/')
]