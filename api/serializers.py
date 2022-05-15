from http.client import HTTPResponse
from lib2to3.pgen2.parse import ParseError
from django.contrib.auth.models import User
from datetime import date
from django.forms import ValidationError
from pkg_resources import require
from rest_framework import serializers, status
from rest_framework.response import Response
from subject.models import Subject
from student.models import Student
from assignment.models import Assignment
from department.models import Department
from exam.models import Exam, SingleExam
from fee.models import Fee
from grade.models import Grade, GradeSubject
from result.models import Result
from staff.models import Staff
from teacher.models import Teacher
from attendance.models import Attendance
from message.models import Message
from notice.models import Notice
from custom_scripts import get_slug

class AttendanceSerializer(serializers.ModelSerializer):
    def get_student_name(self, request, obj):
        st_name = obj.student.name
        return st_name

    class Meta:
        model = Attendance
        fields = ['student', 'is_present']


class SubjectSerializer(serializers.ModelSerializer): 

    # import ipdb; ipdb.set_trace()
    # current_user = serializers.SerializerMethodField('get_user')

    # def get_user(self, obj):
    #     request = self.context.get('request', None)
    #     if request:
    #         return request.user
    # user = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())


    class Meta:
        model = Subject
        
        fields = ['id', 'name']
        read_only_fields = ['created_by', 'slug']  

        # import ipdb; ipdb.set_trace()  

    # def create(self, validated_data):
    #     current_user = validated_data.pop['current_user']
    #     validated_data['created_by'] = current_user
    #     return validated_data
# 
      # import ipdb; ipdb.set_trace()


    def create(self, validated_data):
        slug = get_slug(validated_data)
        sub = Subject(name=validated_data['name'], created_by=self.context['request'].user, slug=slug)        
        sub.save()
        return sub      
        
          
class StudentSerializer(serializers.ModelSerializer):
    
        
    class Meta:
        model = Student
        fields = ['name', 'grade', 'roll_no', 'admission_date', 'phone', 'email', 'dob', 'gender', 'previous_school', 'guardian_name', 'guardian_profession', 'guardian_address', 'guardian_phone', 'is_specially_abled']

    


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'subject', 'grade', 'short_title', 'description', 'submission_date', 'is_active', 'posted_by']
        read_only_fields = ['posted_by', 'is_active']     


    def create(self, validated_data):
        validated_data.pop('posted_by', None)
        assignment = Assignment(            
            **validated_data,
            posted_by =  self.context['request'].user
        )

        assignment.save()
        return assignment

    def validate_submission_date(self, value):
        if value < date.today():
            raise ValidationError('The submission date must be a date after present date.')
        return value

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'created_at', 'created_by']
        read_only_fields = ['created_at', 'created_by']

    def create(self, validated_data):
        department = Department(
            name = validated_data['name'],
            created_by = self.context['request'].user
        )
        department.save()
        return department

class SingleExamSerializer(serializers.ModelSerializer):
    class Meta:
        model: SingleExam
        fields = ['date', 'subject', 'start_time', 'end_time', 'full_marks', 'pass_marks']


class ExamSerializer(serializers.ModelSerializer):
    # exams = SingleExamSerializer()
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


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ['id', 'message_subject', 'body',  'sender', 'receiver', 'is_read']
        
        extra_kwargs = {
            'sender': {'read_only': True}
        }


    def create(self, validated_data):
        validated_data.pop('sender', None)
        message = Message(            
            **validated_data,
            sender =  self.context['request'].user,

        )

        # print(message.sender)
        # print(message.receiver)
        # print(vars(message._state))

        if message.sender ==  message.receiver:
            message.message_subject = "Cannot send message."
            message.body = "Sender and Receiver are the same person"
            return message
        else:
            message.save()
            return message


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id','title', 'description', 'created_by']
        
        extra_kwargs = {
                    'created_by': {'read_only': True},
                }
        

    def create(self, validated_data):
        validated_data.pop('created_by', None)
        notice = Notice(
                **validated_data,
                created_by = self.context['request'].user,
                )
        notice.save()
        return notice


