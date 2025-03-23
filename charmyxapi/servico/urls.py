from django.urls import path
from . import views

urlpatterns = [
    path('api', views.ServicoAPI.as_view(), name='servico-list'),
    path('api/<int:servico_id>', views.ServicoAPI.as_view(), name='servico-detail'),
]