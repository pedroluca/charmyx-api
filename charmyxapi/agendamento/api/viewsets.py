from rest_framework import viewsets
from agendamento.api import serializers
from agendamento.models import Agendamento

class AgendamentoViewSet(viewsets.ModelViewSet):
    serializers_class = serializers.AgendamentoSerializer
    queryset = Agendamento.objects.all()
