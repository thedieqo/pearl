from django.db import models
from inventario.models import Producto
from clientes.models import Cliente

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.nombre} compró {self.cantidad} x {self.producto.nombre}"