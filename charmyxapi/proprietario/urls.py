from rest_framework.routers import DefaultRouter
from .views import ProprietarioViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'proprietarios', ProprietarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
