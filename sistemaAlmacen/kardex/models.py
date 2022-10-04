from django.db import models

# Create your models here. todos los modelos del star uml

class Marca(models.Model):
    marca = models.CharField(max_length=30)

    def __str__(self):
        return self.marca

class Productos(models.Model):
    producto = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)

class Proveedor(models.Model):
    proveedor = models.CharField(max_length=50)
    ruc = models.CharField(max_length=11)
    direcion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=30)

class Producto_Proveedor(models.Model):
     producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
     proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class Unidad_de_Medidas(models.Model):
    tipo_cantidad = models.CharField(max_length=25)

class Caracteristicas_Producto(models.Model):
    preciov = models.DecimalField(max_digits=12,decimal_places=2)
    cantidadv = models.DecimalField(max_digits=12, decimal_places=2)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    unidad_de_medida = models.ForeignKey(Unidad_de_Medidas, on_delete=models.CASCADE)


class Compra(models.Model):
    comprovante=models.CharField(max_length=20)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12,decimal_places=2)

class Compra_Detalle(models.Model):
    compra= models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto_proveedor = models.ForeignKey(Producto_Proveedor, on_delete=models.CASCADE)
    cantidad= models.DecimalField(max_digits=12,decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=12,decimal_places=2)
    subtotal= models.DecimalField(max_digits=12,decimal_places=2)

class Inventario(models.Model):
    fecha_horas = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    movimiento = models.CharField(max_length=1)
    compra_detalle = models.ForeignKey(Compra_Detalle, on_delete=models.CASCADE)
    stock = models.DecimalField(max_digits=12,decimal_places=2)

class Invetariador(models.Model):
    codigo_trabajador = models.CharField(max_length=10)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
