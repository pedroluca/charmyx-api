from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Salao
from .serializers import SalaoSerializer

class SalaoList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        saloes = Salao.objects.all()
        if request.user.groups.filter(name='Proprietarios').exists():
            saloes = saloes.filter(proprietario=request.user)
        serializer = SalaoSerializer(saloes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SalaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(proprietario=request.user.proprietario)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalaoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, salao_id):
        try:
            salao = Salao.objects.get(pk=salao_id)
            serializer = SalaoSerializer(salao)
            return Response(serializer.data)
        except Salao.DoesNotExist:
            return Response({'error': 'Salao not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, salao_id):
        try:
            salao = Salao.objects.get(pk=salao_id)
            serializer = SalaoSerializer(salao, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Salao.DoesNotExist:
            return Response({'error': 'Salao not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, salao_id):
        try:
            salao = Salao.objects.get(pk=salao_id)
            salao.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Salao.DoesNotExist:
            return Response({'error': 'Salao not found'}, status=status.HTTP_404_NOT_FOUND)