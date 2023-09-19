from .models import User
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import Asistencia, Profile


#----------tabla-------resource--------------------------------------------------------------------------------------
class AsistenciaResource(resources.ModelResource):
    class Meta:
        model = Asistencia
# --------------------------------------------------------------------------------------------------------------------

#----------tabla-------resource--------------------------------------------------------------------------------------
class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile
# --------------------------------------------------------------------------------------------------------------------

#----------tabla-------admin------------------------------------------------------------------------------------------
class AsistenciaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('estado','fecha_asistencia','horas')
    list_display = ('User','estado','fecha_asistencia','horas','Cronograma_actividad')
# --------------------------------------------------------------------------------------------------------------------

#----------tabla-------admin------------------------------------------------------------------------------------------
class ProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('documento','Jornada')
    list_display = ('User','documento','Jornada','Rol','Curso')
# --------------------------------------------------------------------------------------------------------------------

admin.site.register(User, UserAdmin)
admin.site.register(Asistencia, AsistenciaAdmin)
admin.site.register(Profile, ProfileAdmin)






















# from.models import User

# # Register your models here.
# admin.site.register(User)