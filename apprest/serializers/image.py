from rest_framework import serializers
from apprest.models.image import CalipsoAvailableImages


class CalipsoImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('public_name', 'image', 'cpu', 'memory', 'hdd')
        model = CalipsoAvailableImages
