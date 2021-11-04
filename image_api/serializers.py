from rest_framework import serializers
from image_api.models import Image

class ImageSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Image
        fields = ['id', 'image']