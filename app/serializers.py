from rest_framework import serializers
from .models import Patient, PatientActivity
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']

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
