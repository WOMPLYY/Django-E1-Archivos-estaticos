from django.db import models

#1 ---------tabla-fuerte-------------------------------------------------------------------------------------------
class Curso(models.Model):
    # id_curso = models.IntegerField(verbose_name='id del curso')
    nombre_curso = models.CharField(max_length=5,verbose_name='Nombre del curso')

    def __str__(self):
        return self.nombre_curso

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        db_table = 'curso'
        ordering = ['id']
#2 ---------tabla-fuerte-------------------------------------------------------------------------------------------

#3 ----tabla-fuerte------------------------------------------------------------------------------------------------
class Rol(models.Model):
    # id_rol = models.IntegerField(verbose_name='id del rol')
    nombre = models.CharField(max_length=45,verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion del rol')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        db_table = 'rol'
        ordering = ['id']