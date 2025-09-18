from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from inventario.views import ProductoViewSet
from clientes.views import ClienteViewSet   # 👈 aquí con minúscula
from ventas.views import VentaViewSet       # 👈 esta ya estaba bien

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'ventas', VentaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]