# from rest_framework import serializers
# from .models import Patient, PatientActivity
#
# class PatientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Patient
#         fields = '__all__'
#
# class PatientActivitySerializer(serializers.ModelSerializer):
#     duration = serializers.SerializerMethodField()
#
#     class Meta:
#         model = PatientActivity
#         fields = '__all__'
#
#     def get_duration(self, obj):
#         return obj.duration()
from rest_framework import serializers
from .models import Patient, PatientActivity

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientActivitySerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()

    class Meta:
        model = PatientActivity
        fields = '__all__'

    def get_duration(self, obj):
        return obj.duration()
