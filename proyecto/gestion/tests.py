from django.test import TestCase
from django.urls import reverse
from .models import Departamento, Empleado, Actividad, Asignacion
from django.contrib.auth import get_user_model

class DepartamentoModelTest(TestCase):
    def test_crear_departamento(self):
        departamento = Departamento.objects.create(nombre="Recursos Humanos", ubicacion="Piso 2")
        self.assertEqual(departamento.nombre, "Recursos Humanos")
        self.assertEqual(departamento.ubicacion, "Piso 2")
        self.assertEqual(str(departamento), "Recursos Humanos")

class EmpleadoModelTest(TestCase):
    def test_crear_empleado(self):
        departamento = Departamento.objects.create(nombre="IT", ubicacion="Piso 3")
        empleado = Empleado.objects.create(nombre="Ana López", correo="ana@gmail.com", departamento=departamento)
        self.assertEqual(empleado.nombre, "Ana López")
        self.assertEqual(empleado.correo, "ana@gmail.com")
        self.assertEqual(empleado.departamento, departamento)

class EmpleadoViewTest(TestCase):
    def setUp(self):
        # Crear datos de prueba
        departamento = Departamento.objects.create(nombre="Recursos Humanos", ubicacion="Piso 2")
        Empleado.objects.create(nombre="Ana López", correo="ana@gmail.com", departamento=departamento)

    def test_listar_empleados(self):
        # Hacer una solicitud GET a la vista listar_empleados
        response = self.client.get(reverse('gestion:listar_empleados'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ana López")
        self.assertContains(response, "ana@gmail.com")

class ActividadEmpleadoViewTest(TestCase):
    def setUp(self):
        # Crear datos de prueba
        departamento = Departamento.objects.create(nombre="Recursos Humanos", ubicacion="Piso 2")
        empleado = Empleado.objects.create(nombre="Ana López", correo="ana@gmail.com", departamento=departamento)
        actividad = Actividad.objects.create(nombre="Desarrollo web", fecha_inicio="2024-03-01")
        Asignacion.objects.create(empleado=empleado, actividad=actividad, fecha_asignacion="2024-03-01", rol="gerente")

    def test_actividad_empleado(self):
        # Hacer una solicitud GET para ver las actividades de un empleado
        empleado = Empleado.objects.get(correo="ana@gmail.com")
        response = self.client.get(reverse('gestion:actividad_empleado', args=[empleado.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Desarrollo web")
        self.assertContains(response, "gerente")
