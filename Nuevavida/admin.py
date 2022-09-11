from django.contrib import admin
from .models import Usuario, Plan, MetodoPago, Documentaciones, Factura

# Register your models here.

@admin.register(Usuario) #decorador
class UsuarioAdmin (admin.ModelAdmin):
    list_display =('cedula','nombre','apellido','correo','telefono','fechaNacimiento') 
    search_fields=['nombre', 'cedula'] 

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display= ('nombrePlan','precio',)
    search_fields =['nombrePlan',]

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display= ('nombreMetodo',)
    search_fields =['nombreMetodo']
    

@admin.register(Documentaciones)
class DocumentacionesAdmin(admin.ModelAdmin):
    list_display= ('docuMedicos','docuAfiliacion','docuInfo')
    search_fields =['docuInfo']



@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display= ('idFactura','metodoPago')
    search_fields =['idFactura']



    