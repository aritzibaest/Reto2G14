from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return f"id={self.id}, nombre={self.nombre}, telefono={self.telefono}"

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"nombre={self.nombre}, antiguedad={self.antiguedad}"

class Empleado(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    habilidades = models.ManyToManyField(Habilidad)
    nombre= models.CharField(max_length = 50)
    fecha_nacimiento = models.DateField()
    antiguedad = models.IntegerField(default=0)

    def __str__(self):
        return f"id={self.id}, nombre={self.nombre}, fecha_nacimiento={self.fecha_nacimiento}, antiguedad={self.antiguedad}"