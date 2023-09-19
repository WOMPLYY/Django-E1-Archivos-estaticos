from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Inventario_herramienta

#------tabla-fuerte-resource----------------------------------------------------------------------------------------
class Inventario_herramientaResource(resources.ModelResource):
    class Meta:
        model = Inventario_herramienta
# -------------------------------------------------------------------------------------------------------------------

#------tabla-fuerte-admin-------------------------------------------------------------------------------------------
class Inventario_herramientaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('nombre','cantidad')
    list_display = ('nombre','cantidad')
# -------------------------------------------------------------------------------------------------------------------

# Register your models here.
admin.site.register(Inventario_herramienta, Inventario_herramientaAdmin)