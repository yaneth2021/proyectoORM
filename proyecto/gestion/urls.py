from django.urls import path
from . import views

app_name='gestion'

urlpatterns=[
    path('empleados/',views.listar_empleados, name='listar_empleados'),
    path('empleados/<int:empleado_id>/actividades/',views.actividad_empleado, name='actividad_empleado'),
    path('actividades/', views.listar_actividades, name='listar_actividades'),  # Agrega esta línea
    path('asignar/',views.asignar_empleado,name='asignar_empleado'),
]