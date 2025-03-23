from rest_framework import serializers
from .models import Proprietario

class ProprietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietario
        fields = ['id', 'username', 'password', 'email', 'nome', 'telefone', 'especializacao']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Proprietario(**validated_data)
        user.set_password(password)
        user.save()
        return user
