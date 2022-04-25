from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'admission_fee', 'monthly_fee', 'transportation_fee', 'other_fee', 'discount']