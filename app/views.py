from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Patient, PatientActivity
from .serializers import PatientSerializer, PatientActivitySerializer
from django.utils import timezone
from django.db.utils import IntegrityError

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'details': 'Not Found'}, status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response(f"passed for {request.user.email}")

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

        # Always create a new session entry for this patient on the same day
        activity = PatientActivity.objects.create(
            patient=patient,
            date=timezone.now().date(),
            start_time=current_time
        )
        activity.save()

        return Response(PatientActivitySerializer(activity).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post', 'get'])
    def end(self, request, pk=None):
        patient = self.get_object()
        current_time = timezone.now().time()

        try:
            # Find the most recent session for this patient on this date that doesn't have an end time
            activity = PatientActivity.objects.filter(
                patient=patient,
                date=timezone.now().date(),
                end_time__isnull=True  # Ensure we pick an open session
            ).latest('start_time')  # Get the latest session by start time

            activity.end_time = current_time
            activity.save()

            return Response(PatientActivitySerializer(activity).data, status=status.HTTP_200_OK)

        except PatientActivity.DoesNotExist:
            return Response({'detail': 'No active session found to end.'}, status=status.HTTP_400_BAD_REQUEST)
