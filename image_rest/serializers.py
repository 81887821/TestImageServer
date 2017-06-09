from rest_framework import serializers
from image_rest.models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'uploader', 'name')
        read_only_fields = ('uploader', )

