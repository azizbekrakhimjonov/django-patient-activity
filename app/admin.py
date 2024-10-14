from django.contrib import admin
from .models import Patient, PatientActivity

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'mobile_number')

# @admin.register(PatientActivity)
# class PatientActivityAdmin(admin.ModelAdmin):
#     list_display = ('mobile_number', 'patient', 'date', 'start_time', 'end_time', 'duration')

@admin.register(PatientActivity)
class PatientActivityAdmin(admin.ModelAdmin):
    list_display = ('patient_mobile_number', 'patient', 'date', 'start_time', 'end_time', 'duration')

    def patient_mobile_number(self, obj):
        return obj.patient.mobile_number

    patient_mobile_number.short_description = 'Mobile Number'


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
