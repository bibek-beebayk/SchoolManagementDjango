from asyncio import BaseTransport
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from django.urls import path
from . import views

router = DefaultRouter()
router.register('subjects', views.SubjectViewSet, basename='subjects')
router.register('students', views.StudentViewSet, basename='students')
router.register('assignments', views.AssignmentViewSet, basename='assignments')
router.register('departments', views.DepartmentViewSet, basename='departments')
router.register('exams', views.ExamViewSet, basename='exams')
router.register('fees', views.FeeViewSet, basename='fees')
router.register('grades', views.GradeViewSet, basename='grades')
router.register('gradesubjects', views.GradeSubjectViewSet, basename='gradesubjects')
router.register('results', views.ResultViewSet, basename='results')
router.register('staffs', views.StaffViewSet, basename='staffs')
router.register('teachers', views.TeacherViewSet, basename='teachers')
router.register('attendance', views.AttendanceViewSet, basename='attendance')
router.register('received-messages', views.ReceivedMessageView, basename='received-messages')
router.register('sent-messages', views.SentMessageView, basename='sent-messages')
router.register('create-message', views.SendMessageView, basename='create-message')
router.register('notices', views.NoticeViewSet, basename='notices')

urlpatterns = router.urls

registration_url = path('register/', views.RegisterView.as_view(), name='register')
# login_url = path('login/', views.LoginView.as_view(), name='login')

schema_url = path('openapi/', get_schema_view(
        title="SchoolManagement API",
        description="API for the School Management System",
        version="1.0.0"
    ), name='openapi-schema')

urlpatterns.append(registration_url)
# urlpatterns.append(login_url)
urlpatterns.append(schema_url)
