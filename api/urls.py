from django.urls import path
from .views import ShortURLViewSet

short_url_list = ShortURLViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

short_url_detail = ShortURLViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('url/', short_url_list),
    path('url/<str:pk>/', short_url_detail),
    path('url/<str:pk>/+/', short_url_detail)
]