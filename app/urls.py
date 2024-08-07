from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

from django.urls import re_path
from . import views

router = DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    re_path('', include(router.urls)),

]