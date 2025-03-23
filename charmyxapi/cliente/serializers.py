from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'username', 'password', 'email', 'nome', 'telefone', 'cpf']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Cliente(**validated_data)
        user.set_password(password)
        user.save()
        return user
