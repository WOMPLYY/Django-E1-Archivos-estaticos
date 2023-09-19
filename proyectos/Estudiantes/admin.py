from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from.models import Curso, Rol

#-----------tabla-fuerte-resource-------------------------------------------------------------------------------------
class CursoResource(resources.ModelResource):
    class Meta:
        model = Curso

#------tabla-fuerte-resource------------------------------------------------------------------------------------------
class RolResource(resources.ModelResource):
    class Meta:
        model = Rol

#-----------tabla-fuerte-admin----------------------------------------------------------------------------------------
class CursoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('codigo_curso','nombre_curso')
    list_display = ('codigo_curso','nombre_curso')
# -------------------------------------------------------------------------------------------------------------------

#------tabla-fuerte-admin---------------------------------------------------------------------------------------------
class RolAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('nombre','descripcion')
    list_display = ('nombre','descripcion')
# -------------------------------------------------------------------------------------------------------------------

admin.site.register(Curso, CursoAdmin)
admin.site.register(Rol, RolAdmin)
