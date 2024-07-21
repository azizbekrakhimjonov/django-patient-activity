from django.contrib import admin
from .models import Patient, PatientActivity

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'mobile_number')

@admin.register(PatientActivity)
class PatientActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'date', 'start_time', 'end_time', 'duration')
# from django.contrib import admin
# from .models import Patient, PatientActivity
#
# @admin.register(Patient)
# class PatientAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'age', 'mobile_number')
#
# @admin.register(PatientActivity)
# class PatientActivityAdmin(admin.ModelAdmin):
#     list_display = ('id', 'patient', 'date', 'start_time', 'end_time', 'duration')
