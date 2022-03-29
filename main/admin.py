from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_header = "MySchool"

@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'middle_name', 'last_name','gender', 'salary', 'specialization']

class GradeSubjectInline(admin.TabularInline):
    model = models.GradeSubject
    extra = 1

@admin.register(models.Grade)
class GradeAdmin(admin.ModelAdmin):
    inlines = [GradeSubjectInline]
    list_display = ['id', 'name', 'room_no', 'student_count', 'class_teacher']


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name', 'grade', 'phone', 'address']

@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'middle_name', 'last_name', 'job_designation', 'joining_date', 'salary']

@admin.register(models.Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'grade', 'short_title', 'submission_date']

@admin.register(models.Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['id', 'grade', 'subject', 'exam_date', 'start_time', 'room_no']


@admin.register(models.Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'admission_fee', 'monthly_fee', 'transportation_fee', 'other_fee', 'discount']

# @admin.register(models.Result)
# class ResultAdmin(admin.ModelAdmin):
#     list_display = ['id', 'student', 'grade', 'total_marks']

class MarkInline(admin.TabularInline):
    model = models.Mark
    extra = 1
    # result = (self, self.obtained_mark)

    # def result(self, mark):
    #     if mark.obtained_mark  >= mark.pass_mark:
    #         return 'Pass'
    #     else:
    #         return 'Fail'


# @admin.register(models.Result)
# class ResultAdmin(admin.ModelAdmin):
#     inlines = [MarksInline]
#     list_display = ['id', 'student']


@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    inlines = [MarkInline]
    list_display = ['student', 'full_marks', 'pass_marks', 'obtained_marks', 'percentage', 'result'] 

@admin.register(models.StaffDepartment)
class StaffDepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'staff', 'department', 'job_description']

