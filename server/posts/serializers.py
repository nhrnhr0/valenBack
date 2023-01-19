from .models import Post

from rest_framework import serializers 
# Serializers define the API representation.
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post 
        fields = ['id', 'title', 'body', 'created_at', 'updated_at', 'is_published', 'header_image', 'slug']