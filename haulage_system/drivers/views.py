from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Driver
from .serializers import DriverSerializer

class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer