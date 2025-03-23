from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Servico
from .serializers import ServicoSerializers
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ServicoAPI(APIView):

    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar

    def get(self, request):
        servicos = Servico.objects.all()
        serializer = ServicoSerializers(servicos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServicoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)