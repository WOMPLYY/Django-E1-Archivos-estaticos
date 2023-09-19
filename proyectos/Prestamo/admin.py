from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Prestamo, Herramienta
# Register your models here.

#-----------tabla-debil-resource--------------------------------------------------------------------------------------
class PrestamoResource(resources.ModelResource):
    class Meta:
        model = Prestamo
# -------------------------------------------------------------------------------------------------------------------

#------------tabla-debil-resource------------------------------------------------------------------------------------
class HerramientaResource(resources.ModelResource):
    class Meta:
        model = Herramienta
# -------------------------------------------------------------------------------------------------------------------

#-----------tabla-debil-admin-----------------------------------------------------------------------------------------
class PrestamoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('estado','descripcion','cantidad')
    list_display = ('User','estado','descripcion','cantidad')
# --------------------------------------------------------------------------------------------------------------------

#------------tabla-debil-admin----------------------------------------------------------------------------------------
class HerramientaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('disponibilidad', 'descripcion')
    list_display = ('Inventario_herramienta','disponibilidad', 'descripcion')
# --------------------------------------------------------------------------------------------------------------------

admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Herramienta, HerramientaAdmin)