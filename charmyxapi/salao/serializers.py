from rest_framework import serializers
from .models import Salao

class SalaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salao
        fields = '__all__'