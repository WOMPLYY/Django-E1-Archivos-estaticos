from django.db import models
from django.contrib.auth.models import AbstractUser
# from ..core.models import Rol, Curso, Prestamo, Asistencia
from Estudiantes.models import Rol, Curso
from Actividades.models import Cronograma_actividad
# from users.models import Customer

class User(AbstractUser):
    pass

class Profile(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    documento = models.IntegerField()
    # jornada = models.TextChoices()
    # class Jornada(models.TextChoices):
    #     mañana = "mañana"
    #     tarde = "tarde"
    # Jornada.JET_SKI.label
    class jornada(models.TextChoices):
        mañana = "mañana"
        tarde = "tarde"
    Jornada = models.TextField(choices=jornada.choices)
    Rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.User.username

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        db_table = 'profile'
        ordering = ['id']

# class Customer(User):
#     class Meta:
#         proxy = True
        
#     def get_usuarios(self):
#         return [] 
    


class Asistencia(models.Model):
    # id_asistencia = models.IntegerField(verbose_name='Asistencia')
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ASISTIO = "asistio"
        INASISTIO = "no asistio"
    estado = models.CharField(choices=Estado.choices,max_length=20, verbose_name='Estado')
    fecha_asistencia = models.DateField(verbose_name='Fecha_asistencia')
    horas = models.IntegerField(verbose_name='Horas')
    Cronograma_actividad = models.ForeignKey(Cronograma_actividad, on_delete=models.CASCADE, verbose_name='Actividad')
    # id_usuario = models.IntegerField(verbose_name='Usuario')


    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        db_table = 'asistencia'
        ordering = ['id']
# from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(AbstractUser):
#     documento = models.IntegerField(verbose_name='Documento')
#     jornada = models.CharField(max_length=15, verbose_name='Jornada')
#     rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
#     curso = models.ForeignKey(Curso, on_delete=models.CASCADE)


    

# class Customer(User):
#     class Meta:
#         proxy = True

#     def get_products(slef):
#         return []
# from django.db import models
# from django.contrib.auth.models import AbstractUser, User
# # from ..core.models import Rol, Curso, Prestamo, Asistencia
# from Estudiantes.models import Rol, Curso
# # from users.models import Customer


# class Customer(User):
#     class Meta:
#         proxy = True
        
    
    
# class User(AbstractUser):
#     User = models.ForeignKey(User, on_delete=models.CASCADE)
#     documento = models.IntegerField()
#     # jornada = models.TextChoices()
#     # class Jornada(models.TextChoices):
#     #     mañana = "mañana"
#     #     tarde = "tarde"
#     # Jornada.JET_SKI.label
#     class jornada(models.TextChoices):
#         mañana = "mañana"
#         tarde = "tarde"
#     Jornada = models.TextField(choices=jornada.choices)
#     Rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
#     Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
# # from django.contrib.auth.models import AbstractUser

# # Create your models here.

# # class User(AbstractUser):
# #     documento = models.IntegerField(verbose_name='Documento')
# #     jornada = models.CharField(max_length=15, verbose_name='Jornada')
# #     rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
# #     curso = models.ForeignKey(Curso, on_delete=models.CASCADE)


    

# # class Customer(User):
# #     class Meta:
# #         proxy = True

# #     def get_products(slef):
# #         return []