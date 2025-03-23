from .models import Proprietario
from rest_framework.viewsets import ModelViewSet
from .serializers import ProprietarioSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
class ProprietarioViewSet(ModelViewSet):
    queryset = Proprietario.objects.all()  
    serializer_class = ProprietarioSerializer 

    def get_permissions(self):
        if self.action == 'create':  # POST
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_queryset(self):
        return Proprietario.objects.filter(id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save()

