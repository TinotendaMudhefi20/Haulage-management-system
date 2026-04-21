from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Truck
from .serializers import TruckSerializer

class TruckViewSet(ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer