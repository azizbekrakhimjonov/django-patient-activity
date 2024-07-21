# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from .models import Patient, PatientActivity
# from .serializers import PatientSerializer, PatientActivitySerializer
# from django.utils import timezone
#
# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer
#
#     @action(detail=True, methods=['post', 'get'])
#     def start(self, request, pk=None):
#         patient = self.get_object()
#         current_time = timezone.now().time()
#         activity, created = PatientActivity.objects.get_or_create(patient=patient, date=timezone.now().date())
#         activity.start_time = current_time
#         activity.save()
#         return Response(PatientActivitySerializer(activity).data, status=status.HTTP_200_OK)
#
#     @action(detail=True, methods=['post', 'get'])
#     def end(self, request, pk=None):
#         patient = self.get_object()
#         current_time = timezone.now().time()
#         activity, created = PatientActivity.objects.get_or_create(patient=patient, date=timezone.now().date())
#         activity.end_time = current_time
#         activity.save()
#         return Response(PatientActivitySerializer(activity).data, status=status.HTTP_200_OK)


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Patient, PatientActivity
from .serializers import PatientSerializer, PatientActivitySerializer
from django.utils import timezone
from django.db.utils import IntegrityError


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        age = request.data.get('age')
        mobile_number = request.data.get('mobile_number')
        try:
            patient, created = Patient.objects.get_or_create(name=name, age=age, mobile_number=mobile_number)
            if not created:
                return Response({'detail': 'Patient already exists.'}, status=status.HTTP_200_OK)
            serializer = self.get_serializer(patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'detail': 'Patient already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post', 'get'])
    def start(self, request, pk=None):
        patient = self.get_object()
        current_time = timezone.now().time()
        activity, created = PatientActivity.objects.get_or_create(patient=patient, date=timezone.now().date())
        activity.start_time = current_time
        activity.save()
        return Response(PatientActivitySerializer(activity).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post', 'get'])
    def end(self, request, pk=None):
        patient = self.get_object()
        current_time = timezone.now().time()
        activity, created = PatientActivity.objects.get_or_create(patient=patient, date=timezone.now().date())
        activity.end_time = current_time
        activity.save()
        return Response(PatientActivitySerializer(activity).data, status=status.HTTP_200_OK)
