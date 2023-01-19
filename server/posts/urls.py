
from .views import PostsViewSet
from django.urls import path

urlpatterns = [
    path('', PostsViewSet.as_view({'get': 'list'}), name='posts'),
]