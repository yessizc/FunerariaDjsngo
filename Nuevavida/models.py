from datetime import date
from pickle import TRUE


from django.db import models

# Create your models here.

class Plan (models.Model):
    nombrePlan = models.CharField(max_length=100)
    precio = models.IntegerField()
    caracteristicas =models.CharField(max_length=1000,null=TRUE)




class Cotizante(models.Model):
    cedula = models.IntegerField(unique= True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField()
    correo = models.EmailField(max_length=250,null=True,blank= True)
    fechaNacimiento = models.DateField()
    idplan = models.ForeignKey(Plan, on_delete= models.DO_NOTHING)
    deuda =models.IntegerField(null=True, default=0)


    #def __str__(self):
        #return f"{self.nombre}"

class Beneficiario (models.Model):
    cedulaBeneficiario= models.IntegerField(unique= True)
    nombreBeneficiario = models.CharField(max_length=100)
    apellidoBeneficiario = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    cedulaCotizante = models.ForeignKey(Cotizante, on_delete= models.DO_NOTHING)

    def __str__(self):
        return f"{self.nombreBeneficiario} {self.cedulaBeneficiario}"




class Factura (models.Model):
    fechaPago= models.DateField(null=TRUE)
    totalDeuda= models.IntegerField(null=TRUE)
    totalPago= models.IntegerField(null=TRUE)

    def __str__ (self):

        return f"{self.fechaPago} {self.totalPago} {self.totalDeuda}"

class Pagos (models.Model):
    valor = models.IntegerField()
    fechaPago = models.DateField()
    cuota =models.IntegerField()
    idFactura = models.ForeignKey(Factura, on_delete= models.DO_NOTHING)
    cedulaCotizante= models.ForeignKey(Cotizante, on_delete= models.DO_NOTHING)

    def __str__ (self):

        return f"{self.cedulaCotizante} {self.cuota} {self.deuda}"

   




def calcularEdad(self): 
        today = date.today() 
        return today.year - self.fechaNacimiento.year - ((today.month, today.day) < (self.fechaNacimiento.month, self.fechaNacimiento.day))
