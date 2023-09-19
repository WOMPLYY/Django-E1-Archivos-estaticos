from django.db import models

#4 ----tabla-fuerte-----------------------------------------------------------------------------------------------
class Wiki(models.Model):
    # id_wiki = models.IntegerField(verbose_name='id de la wiki')
    nombre = models.CharField(max_length=150,verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion')
    referencias_web = models.TextField(verbose_name='Referencias web')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Wiki'
        verbose_name_plural = 'Wikis'
        db_table = 'wiki'
        ordering = ['id']
#5 --------tabla-fuerte------------------------------------------------------------------------------------------
class Zona(models.Model):
    # id_rol = models.IntegerField(verbose_name='id de la zona')
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion de la zona')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'
        db_table = 'zona'
        ordering = ['id']
#8 ------tabla-debil----------------------------------------------------------------------------------------------
class Labor_social(models.Model):
    # id_labor_social = models.IntegerField(verbose_name='id de la labor social')
    nombre = models.CharField(max_length=150,verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripcion')
    # id_wiki = models.IntegerField(verbose_name='Wiki')
    Wiki = models.ForeignKey(Wiki, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Labor social'
        verbose_name_plural = 'Labores sociales'
        db_table = 'labor_social'
        ordering = ['id']
#6 ------tabla-debil----------------------------------------------------------------------------------------------
class Cronograma_actividad(models.Model):
    # id_cro_act = models.IntegerField(verbose_name='Cronograma')
    Labor_social = models.ForeignKey(Labor_social, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(verbose_name='Fecha_inicio')
    fecha_fin = models.DateField(verbose_name='Fecha_fin')
    # id_labor_social = models.IntegerField(verbose_name='Actividad')
    # id_zona = models.IntegerField(verbose_name='Zona')
    Zona = models.ForeignKey(Zona, on_delete=models.CASCADE)


    def __str__(self):
        return self.Labor_social.nombre
#f'Cronograma {self.pk} - Inicio: {self.fecha_inicio}, Fin: {self.fecha_fin}'

    class Meta:
        verbose_name = 'Cronograma actividad'
        verbose_name_plural = 'Cronograma actividades'
        db_table = 'cronograma_actividad'
        ordering = ['id']