from rest_framework import serializers
from .models import Computador

class ComputadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computador
        fields = '__all__'
