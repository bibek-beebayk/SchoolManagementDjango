from django.contrib.auth.models import User
from django.forms import ValidationError
from pkg_resources import require
from rest_framework import serializers
from rest_framework.response import Response
from subject.models import Subject
from student.models import Student
from assignment.models import Assignment
from department.models import Department
from exam.models import Exam
from fee.models import Fee
from grade.models import Grade, GradeSubject
from result.models import Result
from staff.models import Staff
from teacher.models import Teacher


class SubjectSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Subject
        fields = '__all__'
        read_only_fields = ['created_by']    

        

    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class GradeSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeSubject
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)
    

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'confirm_password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):

        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                'password': '  Fields do not match.'
            })

        return attrs

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],

        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=15, required=True)
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(max_length=32, required=True)
#     # confirm_password = serializers.CharField(max_length=32, required=True)

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         # confirm_password = confirm_password
#         instance = User(**validated_data)

#         # if password != confirm_password:
#         #     return Response(
#         #         {
#         #             'message':'The passwords do not match.',
#         #         }
#         #     )
#         if password is not None:
#             instance.set_password(password)

#         instance.save()
#         return instance
