from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Agendamento
from .serializers import AgendamentoSerializer

class AgendamentoAPI(APIView):
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar

    def get(self, request, agendamento_id=None):
        """Lista todos os agendamentos ou retorna um único por ID"""
        if agendamento_id:
            agendamento = get_object_or_404(Agendamento, id=agendamento_id)
            serializer = AgendamentoSerializer(agendamento)
        else:
            agendamentos = Agendamento.objects.all()
            serializer = AgendamentoSerializer(agendamentos, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Cria um novo agendamento"""
        if isinstance(request.data, list):  # Permite criação de múltiplos agendamentos
            serializer = AgendamentoSerializer(data=request.data, many=True)
        else:
            serializer = AgendamentoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, agendamento_id):
        """Atualiza um agendamento existente"""
        agendamento = get_object_or_404(Agendamento, id=agendamento_id)
        serializer = AgendamentoSerializer(agendamento, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, agendamento_id):
        """Exclui um agendamento específico"""
        agendamento = get_object_or_404(Agendamento, id=agendamento_id)
        agendamento.delete()
        return Response({"message": "Agendamento deletado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
