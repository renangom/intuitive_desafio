from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *
# Create your views here.

class SCVViewSet(viewsets.ModelViewSet):
    queryset = SCV.objects.all()
    serializer_class = SCVSerializer   
