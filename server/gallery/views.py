from django.shortcuts import render
from .models import GalleryImage
from .serializers import GalleryImageSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000

# Create your views class UserViewSet(viewsets.ModelViewSet):
class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    pagination_class = LargeResultsSetPagination