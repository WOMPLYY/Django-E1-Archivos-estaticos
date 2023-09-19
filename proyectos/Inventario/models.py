from django.db import models

# Create your models here.
#3 ----tabla-fuerte------------------------------------------------------------------------------------------------
class Inventario_herramienta(models.Model):
    # id_est_her = models.IntegerField(verbose_name='id del curso')
    nombre = models.CharField(max_length=25, verbose_name='Nombre')
    cantidad = models.IntegerField(verbose_name='Cantidad')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Inventario herramienta'
        verbose_name_plural = 'Inventario herramientas'
        db_table = 'inventario_herramienta'
        ordering = ['id']