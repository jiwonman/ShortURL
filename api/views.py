from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
 
from .models import ShortURL
from .serializers import ShortURLSerializer

# Create your views here.

class ShortURLViewSet(viewsets.ModelViewSet):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer