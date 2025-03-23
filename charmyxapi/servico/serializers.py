from rest_framework import serializers
from .models import Servico


class ServicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'