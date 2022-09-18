from django.urls import path
from Nuevavida.models import Cotizante
from .vistas import cotizanteviews, planviews




 
app_name= "Nuevavida"
urlpatterns = [
    path('', cotizanteviews.index,name="index"), 

    # crud cotizantes
    
    path('Cotizante/',cotizanteviews.listarCotizante, name="listarCotizante"),
    path('editarCotizante/<int:id>',cotizanteviews.editarCotizante, name="editarCotizante"),
    path ('formularioCotizante/<int:id>',cotizanteviews.formularioCotizante, name="formularioCotizante"),
    path ('agregarCotizante/',cotizanteviews.guardarCotizante, name="agregarCotizante"),
    path('eliminarCotizante/<int:id>',cotizanteviews.eliminarCotizante, name="eliminarCotizante"),


    # crud Plan

    path('listarPlan/',planviews.listarPlan, name="listarPlan"),
    path('editarPlan/<int:id>',planviews.editarPlan, name="editarPlan"),
    path ('formularioPlan/<int:id>',planviews.formularioPlan, name="formularioPlan"),
    path ('guardarPlan/',planviews.guardarPlan, name="guardarPlan"),
    path('eliminarPlan/<int:id>',planviews.eliminarPlan, name="eliminarPlan"),


    

    #crud Documentaciones

    #path('Documentaciones/',views.listarDocumentaciones, name="agregarDocumentaciones"),
    #path('Documentaciones/',views.listarDocumentaciones, name="editarDocumentaciones"),
    #path ('formularioDocumentaciones/<int:id>',views.formularioDocumentaciones, name="formularioDocumentaciones"),
    #path ('guardarDocumentaciones/',views.guardarMetodoPago, name="guardaroPlan"),
    #path('eliminarDocumentaciones/<int:id>',views.eliminarDocumentaciones, name="eliminarDocumentaciones"),

    # crud Factura

    #path('Factura/',views.listarDFactura, name="agregarFactura"),
    #path('Factura/',views.listarFactura, name="editarFactura"),
    #path ('formularioFactura/<int:id>',views.formularioFactura, name="formularioFactura"),
    #path ('guardarFacturas/',views.guardarFactura, name="guardarFactura"),
    #path('eliminarFactura/<int:id>',views.eliminarFactura, name="eliminarFactura"),









]


