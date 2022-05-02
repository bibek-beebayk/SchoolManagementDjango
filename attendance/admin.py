from django.contrib import admin
from .models import Attendance

# Register your models here.

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'is_present', 'get_phone']
    list_editable = ['is_present']
    list_filter = ['date', 'is_present', 'student__grade']
    search_fields = ['student__name']
    serach_help_text = 'Name of Student to search'

    def get_queryset(self, request):
        return super().get_queryset(request)

    # def get_fields(self, request, obj):
    #     ph = obj.student_phone
    #     return ph


    @admin.display(description='Phone')
    def get_phone(self, obj):
        phone = obj.student.phone
        return phone

    # get_phone.short_description = 'Phone'