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
from grade.models import Grade
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

    class Meta:
        model = Subject
        
        fields = ['id', 'name']
        read_only_fields = ['created_by', 'slug']  


    def create(self, validated_data):
        slug = get_slug(validated_data)
        sub = Subject(name=validated_data['name'], created_by=self.context['request'].user, slug=slug)        
        sub.save()
        return sub      
        
          
class StudentSerializer(serializers.ModelSerializer):    
        
    class Meta:
        model = Student
        fields = ['name', 'grade', 'roll_no', 'admission_date', 'phone', 'email', 'dob', 'gender', 'previous_school', 'guardian_name', 'guardian_profession', 'guardian_address', 'guardian_phone', 'is_specially_abled']    

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'mobile_number', 'address', 'email', 'joined_on', 'salary', 'gender', 'specialization', 'proficient_subjects', 'dob']

        extra_kwargs = {
            'id' : {
                'read_only' : False,
                'required' : False
            }
        }

class GradeSerializer(serializers.ModelSerializer):
    class_teacher = TeacherSerializer()
    class Meta:
        model = Grade
        fields = ['id', 'name', 'class_teacher']

    def create(self, validated_data):

        validated_data.pop('class_teacher')

        grade = Grade.objects.create(**validated_data)

        class_teacher = self.context['request'].data.get('class_teacher')

        import ipdb; ipdb.set_trace()
        
        if class_teacher.get('id'):
            grade.class_teacher = Teacher.objects.get(id=class_teacher.get('id'))
        else:
            grade.class_teacher  = Teacher.objects.create(**class_teacher)




        return grade

class AssignmentSerializer(serializers.ModelSerializer):
    grade = GradeSerializer()
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




class GradeSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
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


