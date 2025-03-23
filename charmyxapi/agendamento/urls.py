from django.urls import path
from . import views

urlpatterns = [
    path('api', views.AgendamentoAPI.as_view(), name='agendamento-list'),
    path('api/<int:agendamento_id>', views.AgendamentoAPI.as_view(), name='agendamento-detail'),
]