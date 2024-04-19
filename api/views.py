from django.shortcuts import render, redirect

from rest_framework import viewsets, status
from rest_framework.response import Response
 
from .models import ShortURL
from .utils import Base62
from .serializers import ShortURLSerializer

# Create your views here.
_origin_domain = 'http://127.0.0.1:8001/api/url/'

class ShortURLViewSet(viewsets.ModelViewSet):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

    # def list(self, request):
    #     pass

    def create(self, request, *args, **kwargs):
        url = request.data.get('url')

        key = Base62().encode()
        obj = ShortURL.objects.filter(url=url).first()

        if obj:
            key = ShortURLSerializer(obj).data['key']
            return Response({'key': key}, status=status.HTTP_200_OK)

        else:
            # URL KEY CHECK 
            while ShortURL.objects.filter(key=key).exists():
                key = Base62().encode()

        serializer = self.get_serializer(data={**request.data, 'url': url, 'key': key})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response({'key': key}, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        instance.count += 1
        instance.save()

        serializer = self.get_serializer(instance)
        redirect_url = serializer.data.get('url')
        return redirect(redirect_url)

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass