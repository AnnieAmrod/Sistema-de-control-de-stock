from django.db import models

etiqueta_choice = (
    ('Unidad', 'Unidad/es'),
    ('Bote', 'Bote/s'),
    ('Bandeja', 'Bandeja/s'),
    ('Brick', 'Brick/s'),
    ('Tableta', 'Tableta/s'),
    ('Botella', 'Botella/s'),
    ('Lata', 'Lata/s'),
    ('Tarro', 'Tarro/s'),
    ('Taza', 'Taza/s'),
    ('Tubo', 'Tubo/s'),
    ('Bolsa', 'Bolsa/s'),
    )


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.nombre


class Stock(models.Model):
    #categoria = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True)
    nombre_producto = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(default=0, blank=True, null=True)
    etiqueta = models.CharField(max_length=50, blank=True, null=True, choices=etiqueta_choice)
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
    creado_por = models.CharField(max_length=50, blank=True, null=True)#Todo cambiar para que tenga más sentido, igual siendo la receta en que se ha gastado o algo así
    punto_de_pedido = models.IntegerField(default=0, blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    #exportar_csv = models.BooleanField(default=False)
    fecha_caducidad = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    
    def __str__(self):
        return self.nombre_producto + ' - ' + str(self.cantidad) + ' ' + self.etiqueta