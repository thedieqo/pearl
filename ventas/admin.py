from django.contrib import admin
from .models import Venta

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ("cliente", "producto", "cantidad", "fecha_venta")
    list_filter = ("fecha_venta", "producto")
    search_fields = ("cliente__nombre", "producto__nombre")