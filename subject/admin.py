from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug', 'created_by']
    # list_editable = ['slug']
    def get_user(request):
        user = request.get_user
        return user

    prepopulated_fields = {'slug': ('name',)}

    

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

