from .models import GalleryImage

from rest_framework import serializers 
# Serializers define the API representation.
class GalleryImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'alt', 'image', 'created_at', 'updated_at', 'location', 'address',]
        