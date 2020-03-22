from rest_framework.serializers import ModelSerializer
from . models import *

class ImageUploadSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"