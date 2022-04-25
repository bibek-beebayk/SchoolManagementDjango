from django.shortcuts import render
import django_filters.rest_framework
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics, authentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from grade.models import Grade, GradeSubject
from subject.models import Subject
from student.models import Student
from assignment.models import Assignment
from department.models import Department
from exam.models import Exam
from fee.models import Fee
from result.models import Result
from staff.models import Staff
from teacher.models import Teacher
from . import serializers
from .custom_paginations import MyPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination
from .custom_filters import IsOwnerFilterBackend
from .custom_permission import RestrictDelete


# Create your views here.
class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SubjectSerializer
    # queryset = Subject.objects.all().order_by('-created_at')

    pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    # pagination_class = MyCursorPagination

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['^name']

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'created_at']
    ordering = ['name'] # default ordering field

    # filter_backends = [IsOwnerFilterBackend]
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [RestrictDelete]


    def get_queryset(self):
        return Subject.objects.all()
        

    

class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication. BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['grade', 'gender']
    throttling_classes = [AnonRateThrottle, UserRateThrottle]



class GradeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GradeSerializer
    queryset = Grade.objects.all()

class GradeSubjectViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GradeSubjectSerializer
    queryset = GradeSubject.objects.all()


class ExamViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ExamSerializer
    queryset = Exam.objects.all()

class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AssignmentSerializer
    queryset = Assignment.objects.all()

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DepartmentSerializer
    queryset = Department.objects.all()

class FeeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FeeSerializer
    queryset = Fee.objects.all()

class ResultViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ResultSerializer
    queryset = Result.objects.all()

class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StaffSerializer
    queryset = Staff.objects.all()

class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TeacherSerializer
    queryset = Teacher.objects.all()

class RegisterView(generics.CreateAPIView):
    
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


# class LoginView(APIView):
#     '''Endpoint for User Login'''
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']
#         user = User.objects.filter(username=username).first()
#         print(user)

#         if user is None:
#             raise AuthenticationFailed('User Not Found!')
        
#         if not user.check_password(password):
#             raise AuthenticationFailed('Incorrect Password!')

#         # payload = {
#         #     'id': user.id,
#         #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#         #     'iat': datetime.datetime.utcnow()
#         # }

#         # token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

#         return Response(
#             {
#                 'message': 'Success'
#             }
#         )

    