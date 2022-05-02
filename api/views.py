from cgitb import lookup
from django.forms import ValidationError
from django.shortcuts import render
import django_filters.rest_framework
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics, authentication, mixins
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
from attendance.models import Attendance
from message.models import Message
from . import serializers
from .custom_paginations import MyPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination
from .custom_filters import IsOwnerFilterBackend
from .custom_permission import RestrictDelete, RestrictUpdate, ViewAssignmentPermission


# Create your views here.
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]


class SubjectViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = serializers.SubjectSerializer
    # queryset = Subject.objects.all().order_by('-created_at')

    pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    # pagination_class = MyCursorPagination

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['^name']

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'created_at']
    ordering = ['-created_at'] # default ordering field

    # filter_backends = [IsOwnerFilterBackend]
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [RestrictDelete, RestrictUpdate, ViewAssignmentPermission]

    # import ipdb; ipdb.set_trace()


    def get_queryset(self):
        return Subject.objects.all()
        
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)        
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     current_user = serializer.pop['current_user']
    #     serializer.created_by = current_user
    #     serializer.save()

    

class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication. BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['grade', 'gender']
    throttling_classes = [AnonRateThrottle, UserRateThrottle]
    lookup_field = 'slug'

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
    # queryset = Assignment.objects.all()
    pagination_class = MyPageNumberPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Assignment.objects.all()
            return Assignment.objects.filter(posted_by=self.request.user)
        return Assignment.objects.filter(id=None)

    

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


class SentMessageView(viewsets.ModelViewSet):

    permission_classes = ['IsAuthenticated']
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        qs = Message.objects.filter(sender=self.request.user)
        return qs


class ReceivedMessageView(viewsets.ModelViewSet):
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        qs = Message.objects.filter(receiver=self.request.user)
        return qs

    


    
