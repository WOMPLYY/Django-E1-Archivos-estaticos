from django.contrib import admin
# Register your models here.
# from.models import Category, Product
from.models import Asistencia, Cronograma_actividad, Curso, Categoria_herramienta, Prestamo, Herramienta, Labor_social, Rol, Wiki, Zona

# admin.site.register(Category)
# admin.site.register(Product)
# Register your models here.

admin.site.register(Asistencia)
admin.site.register(Cronograma_actividad)
admin.site.register(Curso)
admin.site.register(Categoria_herramienta)
admin.site.register(Prestamo)
admin.site.register(Herramienta)
admin.site.register(Labor_social)
admin.site.register(Rol)
admin.site.register(Wiki)
admin.site.register(Zona)