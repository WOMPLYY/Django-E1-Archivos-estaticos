from django.db import models
from users.models import User
from Inventario.models import Inventario_herramienta
#3 ----tabla-debil------------------------------------------------------------------------------------------------
class Herramienta(models.Model):
    # id_inv_her = models.IntegerField(verbose_name='id del inventario de la herramieta'
    # nombre = models.CharField(max_length=50,verbose_name='Nombre de la ')
    Inventario_herramienta = models.ForeignKey(Inventario_herramienta, on_delete=models.CASCADE)
    # nombre = models.CharField(max_length=25, verbose_name='Nombre')
    class Disponibilidad(models.TextChoices):
        DISPONIBLE = "disponible"
        NODISPONIBLE = "no disponible"
    disponibilidad = models.CharField(choices=Disponibilidad.choices,max_length=15, verbose_name='Disponibilidad')
    descripcion = models.TextField(verbose_name='Descripcion')

    def __str__(self):
        return self.Inventario_herramienta.nombre

    class Meta:
        verbose_name = 'Herramienta'
        verbose_name_plural = 'Herramientas'
        db_table = 'herramienta'
        ordering = ['id']
#3 ----tabla-debil------------------------------------------------------------------------------------------------
class Prestamo(models.Model):
    # id_usuario = models.IntegerField(verbose_name='Id del usuario')
    # id_his_her = models.IntegerField(verbose_name='Id de el historico')
    # fecha_entrega = models.DateField(verbose_name='Fecha entrega')
    # fecha_devolucion = models.DateField(verbose_name='Fecha devolucion')
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO = "activo"
        INACTIVO = "inactivo"

    estado = models.CharField(choices=Estado.choices,max_length=20, verbose_name='Estado')
    herramienta = models.ManyToManyField(Herramienta)
    descripcion = models.TextField(verbose_name='Descripcion')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    # id_inv_her = models.IntegerField(verbose_name='Id del inventario de la herramienta')

    def __str__(self):
        return self.User.username

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        db_table = 'prestamo'
        ordering = ['id']


