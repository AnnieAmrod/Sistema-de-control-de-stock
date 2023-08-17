from django.db import models

# Create your models here.
class Stock(models.Model):
    categoria = models.CharField(max_length=50, blank=True, null=True)
    nombre_producto = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(default=0, blank=True, null=True)
    etiqueta = models.CharField(max_length=50, blank=True, null=True)
    cantidad_comprada = models.IntegerField(default=0, blank=True, null=True)
    #cantidad_recibida = models.IntegerField(default=0, blank=True, null=True)
    proveedor = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    precio = models.IntegerField(default=0, blank=True, null=True)
    cantidad_gastada = models.IntegerField(default=0, blank=True, null=True)
    #cantidad_entregada = models.IntegerField(default=0, blank=True, null=True)
    #vendedor = models.CharField(max_length=50, blank=True, null=True)
    gastado_por = models.CharField(max_length=50, blank=True, null=True)
    comprador = models.CharField(max_length=50, blank=True, null=True)
    creado_por = models.CharField(max_length=50, blank=True, null=True)
    punto_de_pedido = models.IntegerField(default=0, blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    exportar_csv = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre_producto + ' - ' + str(self.cantidad) + ' ' + self.etiqueta