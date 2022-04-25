from django.contrib import admin
from . import models
# Register your models here.

class MarkInline(admin.TabularInline):
    model = models.Mark
    extra = 0
    readonly_fields = ('subject_result',)

    def subject_result(self, obj):
        if obj.obtained_mark < obj.pass_mark:
            return 'Fail'
        return 'Pass'



@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    inlines = [MarkInline]
    list_display = ['student', 'full_marks', 'pass_marks', 'obtained_marks', 'percentage', 'result']
    readonly_fields = ['percentage']

    # def percentage(self, obj):
    #     return ((obj.obtained_marks/obj.full_marks)*100)
    
