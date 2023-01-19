from django.shortcuts import render
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from server.settings import MEDIA_URL
import os
# from server.core.decorators import user_is_superuser

from .serializers import PostSerializer
from .models import Post
# Create your views here.
# ViewSets define the view behavior.
class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

