from .models import Cliente
from rest_framework.viewsets import ModelViewSet
from .serializers import ClienteSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_permissions(self):
        if self.action == 'create': 
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_queryset(self):
        return Cliente.objects.filter(id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save()
