from datetime import date
from django.db import models

# Create your models here.



class Usuario(models.Model):
    cedula = models.IntegerField(unique= True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField()
    correo = models.EmailField(max_length=250,null=True,blank= True)
    fechaNacimiento = models.DateField()
   


    def __str__(self):
        return f"{self.nombre}"


class Plan (models.Model):
    idPlan = models.IntegerField(unique=True)
    nombrePlan = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombrePlan} {self.precio}"

class MetodoPago (models.Model):
    nombreMetodo = models.CharField(max_length=100)
    

    def __str__(self):

        return f"{self.nombreMetodo}"



class Documentaciones (models.Model):
    idDocuementaciones = models.IntegerField(unique= True)
    docuMedicos = models.CharField (max_length=1000)
    docuAfiliacion = models.CharField (max_length=1000)
    docuInfo = models.CharField (max_length=1000)

    def __str__ (self):
        return f"{self.docuMedicos} {self.docuAfiliacion} {self.docuInfo}"

class Factura (models.Model):
    idFactura = models.IntegerField(unique= True)
    metodoPago =models.ForeignKey(MetodoPago, on_delete= models.DO_NOTHING)

    def __str__ (self):

        return f"{self.idFactura} {self.metodoPago}"



def calcularEdad(self): 
        today = date.today() 
        return today.year - self.fechaNacimiento.year - ((today.month, today.day) < (self.fechaNacimiento.month, self.fechaNacimiento.day))
