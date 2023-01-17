from .views import GalleryImageViewSet
from django.urls import path

urlpatterns = [
    path('', GalleryImageViewSet.as_view({'get': 'list'}), name='gallery'),
]