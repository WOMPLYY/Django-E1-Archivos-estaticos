from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from.models import Cronograma_actividad, Labor_social, Wiki, Zona

# Register your models here.

#--------tabla-debil-resource----------------------------------------------------------------------------------------
class Cronograma_actividadResource(resources.ModelResource):
    class Meta:
        model = Cronograma_actividad
# -------------------------------------------------------------------------------------------------------------------

#--------tabla-debil-resource----------------------------------------------------------------------------------------
class Labor_socialResource(resources.ModelResource):
    class Meta:
        model = Labor_social
# -------------------------------------------------------------------------------------------------------------------

#------tabla-fuerte-resource------------------------------------------------------------------------------------------
class WikiResource(resources.ModelResource):
    class Meta:
        model = Wiki
# -------------------------------------------------------------------------------------------------------------------

#----------tabla-fuerte-resource--------------------------------------------------------------------------------------
class ZonaResource(resources.ModelResource):
    class Meta:
        model = Zona
# -------------------------------------------------------------------------------------------------------------------

#--------tabla-debil-admin--------------------------------------------------------------------------------------------
class Cronograma_actividadAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('fecha_inicio','fecha_fin')
    list_display = ('Labor_social','fecha_inicio','fecha_fin','Zona')
# -------------------------------------------------------------------------------------------------------------------

#--------tabla-debil-admin--------------------------------------------------------------------------------------------
class Labor_socialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('nombre','descripcion','Wiki')
    list_display = ('nombre','descripcion','Wiki')
# -------------------------------------------------------------------------------------------------------------------

#------tabla-fuerte-admin---------------------------------------------------------------------------------------------
class WikiAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('nombre','descripcion','referencias_web')
    list_display = ('nombre','descripcion','referencias_web')
# -------------------------------------------------------------------------------------------------------------------

#----------tabla-fuerte-admin-----------------------------------------------------------------------------------------
class ZonaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('nombre','descripcion')
    list_display = ('nombre','descripcion')
# -------------------------------------------------------------------------------------------------------------------

admin.site.register(Cronograma_actividad, Cronograma_actividadAdmin)
admin.site.register(Labor_social, Labor_socialAdmin)
admin.site.register(Wiki, WikiAdmin)
admin.site.register(Zona, ZonaAdmin)