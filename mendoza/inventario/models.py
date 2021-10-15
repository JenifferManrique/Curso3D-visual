from django.db import models

# Create your models here.
class grupo(models.Model):
    gruponombre=models.CharField(max_length=150)
    estado = (
        ('1', 'Activo'),
        ('0', 'No Activo'),
    )

    grupoanulado = models.CharField(max_length=1, choices=estado, help_text="Seleccione el estado", default='1')
    def __str__(self):
        return self.gruponombre

class producto(models.Model):
    productogrupo = models.ForeignKey(grupo, on_delete=models.CASCADE)
    productonombre = models.CharField(max_length=150)
    productopreciovta = models.FloatField()
    productocodigo = models.CharField(max_length=50)
    productoexistencia = models.IntegerField()
    estado = (
        ('1', 'Activo'),
        ('0', 'No Activo'),
    )
    productoanulado = models.CharField(max_length=1, choices=estado, help_text="Seleccione el estado", default='1')


class proveedor(models.Model):
    proveedorcedula = models.CharField(max_length=13)
    proveedornombres = models.CharField(max_length=150)
    proveedortelefono = models.CharField(max_length=50)
    estado = (
        ('1', 'Activo'),
        ('0', 'No Activo'),
    )

    proveedoranulado = models.CharField(max_length=1, choices=estado, help_text="Seleccione el estado", default='1')

class cliente(models.Model):
    clientecedula = models.CharField(max_length=13)
    clientenombre = models.CharField(max_length=150)
    clientetelefono = models.CharField(max_length=50)
    estado = (
        ('1', 'Activo'),
        ('0', 'No Activo'),
    )

    clienteanulado = models.CharField(max_length=1, choices=estado, help_text="Seleccione el estado", default='1')

class comprasEnc(models.Model):
    comprasEncproveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)
    comprasEncfechacompra = models.DateField(null=True, blank=True)
    comprasEncobservacion = models.CharField(max_length=150)
    comprasnofactura = models.CharField(max_length=50)
    comprasEncfechafactura = models.DateField()
    comprasEncsubtotal = models.FloatField(default=0)
    comprasEncdescuento = models.FloatField(default=0)
    comprasEnctotal = models.FloatField(default=0)


class comprasdetalle(models.Model):
    comprasdetallecomprasEnc = models.ForeignKey(comprasEnc, on_delete=models.CASCADE)
    comprasdetalleproducto = models.ForeignKey(producto, on_delete=models.CASCADE)
    comprasdetallecantidad = models.IntegerField()
    comprasdetalleprecio = models.FloatField()
    comprasdetallesubtotal = models.FloatField()
    comprasdetalledescuento = models.FloatField()
    comprasdetalletotal = models.FloatField()

class ventaEnc(models.Model):
    ventaEncliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    ventasEncfechaventa = models.DateField(null=True, blank=True)
    ventaEncobservacion = models.CharField(max_length=150)
    ventanofactura = models.CharField(max_length=50)
    ventaEncfechafactura = models.DateField()
    ventaEncsubtotal = models.FloatField(default=0)
    ventaEncdescuento = models.FloatField(default=0)
    ventaEnctotal = models.FloatField(default=0)

class ventasdetalle(models.Model):
    ventadetalleventaEnc = models.ForeignKey(ventaEnc, on_delete=models.CASCADE)
    ventadetalleproducto = models.ForeignKey(producto, on_delete=models.CASCADE)
    ventadetallecantidad = models.IntegerField()
    ventadetalleprecio = models.FloatField()
    ventadetallesubtotal = models.FloatField()
    ventadetalledescuento = models.FloatField()
    ventadetalletotal = models.FloatField()



