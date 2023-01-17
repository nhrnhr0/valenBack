
from django.urls import path

from .views import upload_image, image_list
urlpatterns = [
    path('upload_image', upload_image, name='upload_image'),
    path('image_list', image_list, name='image_list'),
]