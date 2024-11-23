from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre=models.CharField(max_length=100)
    ubicacion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Empleado(models.Model):
    nombre=models.CharField(max_length=100)
    correo=models.EmailField(unique=True)
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre=models.CharField(max_length=200)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField(null=True,blank=True)
    
    def __str__(self):
        return self.nombre
    
class Asignacion(models.Model):
    empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    actividad=models.ForeignKey(Actividad, on_delete=models.CASCADE)
    fecha_asignacion=models.DateField()
    rol=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.empleado.nombre} - {self.actividad.nombre}"
    


    

    