from django.contrib import admin
from .models import Departamento, Empleado, Actividad, Asignacion
# Register your models here.
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display=('nombre','ubicacion')
    
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=('nombre','correo','departamento')
    
@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display=('nombre','fecha_inicio','fecha_fin')
    
@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display=('empleado','actividad','fecha_asignacion','rol')

    