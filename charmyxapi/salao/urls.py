from django.urls import path
from .views import SalaoList, SalaoDetail

urlpatterns = [
    path('', SalaoList.as_view(), name='salao_list'),
    path('<int:salao_id>/', SalaoDetail.as_view(), name='salao_detail'),
]