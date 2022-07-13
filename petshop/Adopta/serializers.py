from rest_framework import serializers
from .models import Adopta

class AdoptaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopta
        fields = '__all__'
