from django.shortcuts import render
from .models import Departamento, Empleado, Actividad, Asignacion
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def listar_empleados(request):
    empleados=Empleado.objects.select_related('departamento').all()
    #ORM    
    #SELECT * FROM empleados JOIN departamentos ON empleados.departamento_id=departamentos.id
    return render(request,'gestion/empleados.html',{'empleados':empleados})

def actividad_empleado(request, empleado_id):
    actividades=Actividad.objects.filter(asignacion__empleado_id=empleado_id)
    #SELECT actividades.* FROM actividades JOIN asignaciones ON actividades.actividad_id WHERE asignaciones.empleado_id=empleado_id 
    return render(request,'gestion/actividades.html', {'actividades':actividades})

def listar_actividades(request):
    # Obtiene todas las actividades ordenadas por fecha de inicio
    actividades = Actividad.objects.all().order_by('fecha_inicio')
    return render(request, 'gestion/actividades.html', {'actividades': actividades})


def asignar_empleado(request):
    try:
        # Obtener el departamento
        departamento = Departamento.objects.get(nombre="Recursos Humanos")
    except ObjectDoesNotExist:
        return render(request, 'gestion/error.html', {'mensaje': 'El departamento Recursos Humanos no existe.'})

    # Crear el empleado solo si no existe
    empleado, creado = Empleado.objects.get_or_create(
        correo="ana@gmail.com",
        defaults={'nombre': "Ana López", 'departamento': departamento}
    )

    # Verificar la actividad
    try:
        actividad = Actividad.objects.get(nombre="Desarrollo web")
    except ObjectDoesNotExist:
        return render(request, 'gestion/error.html', {'mensaje': 'La actividad "Desarrollo web" no existe.'})

    # Crear la asignación
    asignacion = Asignacion.objects.create(
        empleado=empleado,
        actividad=actividad,
        fecha_asignacion="2024-03-01",
        rol="gerente"
    )

    return render(request, 'gestion/asignacion.html', {'empleado': empleado, 'actividad': actividad, 'asignacion': asignacion})
