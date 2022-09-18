from django.contrib import admin
from .models import Cotizante, Plan,  Factura, Beneficiario, Pagos


# Register your models here.

@admin.register(Cotizante) #decorador
class CotizanteAdmin (admin.ModelAdmin):
    list_display =('cedula','nombre','apellido','correo','telefono','fechaNacimiento') 
    search_fields=['nombre', 'cedula'] 


@admin.register(Beneficiario)
class BeneficiarioAdmin (admin.ModelAdmin):
    list_display = ('cedulaBeneficiario','nombreBeneficiario','apellidoBeneficiario','fechaNacimiento','cedulaCotizante')
    search_fields =['nombreBeneficiario','cedulaBeneficiario']



@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display= ('nombrePlan','precio','caracteristicas')
    search_fields =['nombrePlan',]


    


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display= ('fechaPago','totalDeuda','totalPago')
    search_fields =['totalPago']


@admin.register(Pagos)
class PagosAdmin (admin.ModelAdmin):
    list_display = ('valor','fechaPago','cuota','deuda','idFactura','cedulaCotizante')
    search_fields = ['cedulaCotizante','fechaPago','deuda', 'valor']



    