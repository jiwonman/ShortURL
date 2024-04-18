from django.shortcuts import render, redirect

from rest_framework import viewsets
from rest_framework.response import Response
 
from .models import ShortURL
from .serializers import ShortURLSerializer

# Create your views here.

class ShortURLViewSet(viewsets.ModelViewSet):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        redirect_url = serializer.data.get('url')
        return redirect(redirect_url)

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass