from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Produto
from .serializers import ProdutoSerializer
from salao.models import Salao

class ProdutoList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, salao_id):
        produtos = Produto.objects.filter(salao=salao_id)
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request, salao_id):
        try:
            salao = Salao.objects.get(pk=salao_id)
            serializer = ProdutoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(salao=salao)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Salao.DoesNotExist:
            return Response({'error': 'Salao not found'}, status=status.HTTP_404_NOT_FOUND)

class ProdutoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, salao_id, produto_id):
        try:
            produto = Produto.objects.get(pk=produto_id, salao_id=salao_id)
            serializer = ProdutoSerializer(produto)
            return Response(serializer.data)
        except Produto.DoesNotExist:
            return Response({'error': 'Produto not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, salao_id, produto_id):
        try:
            produto = Produto.objects.get(pk=produto_id, salao_id=salao_id)
            serializer = ProdutoSerializer(produto, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Produto.DoesNotExist:
            return Response({'error': 'Produto not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, salao_id, produto_id):
        try:
            produto = Produto.objects.get(pk=produto_id, salao_id=salao_id)
            produto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Produto.DoesNotExist:
            return Response({'error': 'Produto not found'}, status=status.HTTP_404_NOT_FOUND)