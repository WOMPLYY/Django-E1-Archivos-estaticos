from django.contrib import admin
# Register your models here.
# from.models import Category, Product
from.models import Asistencia, Cronograma_actividades, Curso, Estado_herramienta, Historico_herramientas, Inventario_herramientas, Labor_social, Rol, Wiki, Zona

# admin.site.register(Category)
# admin.site.register(Product)
# Register your models here.

admin.site.register(Asistencia)
admin.site.register(Cronograma_actividades)
admin.site.register(Curso)
admin.site.register(Estado_herramienta)
admin.site.register(Historico_herramientas)
admin.site.register(Inventario_herramientas)
admin.site.register(Labor_social)
admin.site.register(Rol)
admin.site.register(Wiki)
admin.site.register(Zona)