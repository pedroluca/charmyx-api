from django.urls import path
from .views import ProdutoList, ProdutoDetail

urlpatterns = [
    path('<int:salao_id>/', ProdutoList.as_view(), name='produto_list'),
    path('<int:salao_id>/<int:produto_id>/', ProdutoDetail.as_view(), name='produto_detail'),
]