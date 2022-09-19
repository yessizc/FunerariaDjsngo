from django.urls import path
from Nuevavida.models import Cotizante
from .vistas import cotizanteviews, planviews, facturaviews, pagosviews, beneficiarioviews




 
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


    
    # crud Factura

    path('Factura/',facturaviews.listarFactura, name="listarFactura"),
    path('verFactura/<int:id>',facturaviews.verFactura, name="verFactura"),
    path('verFacturaPago/<int:id>',facturaviews.verFacturaPago, name="verFacturaPago"),
    path ('descargarFactura/<int:id>',facturaviews.descargarFactura, name="descargarFactura"),


    #crud Pagos

    path('Pagos/',pagosviews.listarPagos, name="listarPagos"),
    path ('formularioPagos/',pagosviews.formularioPagos, name="formularioPagos"),
    path ('agregarPagos/',pagosviews.guardarPagos, name="agregarPagos"),
    path ('buscarCotizante/',pagosviews.buscarCotizante, name="buscarCotizante"),

#crud Beneficiarios

    path('Beneficiario/',beneficiarioviews.listarBeneficiario, name="listarBeneficiario"),
    path('editarBeneficiario/<int:id>',beneficiarioviews.editarBeneficiario, name="editarBeneficiario"),
    path ('formularioBeneficiario/<int:id>',beneficiarioviews.formularioBeneficiario, name="formularioBeneficiario"),
    path ('agregarBeneficiario/',beneficiarioviews.guardarBeneficiario, name="agregarBeneficiario"),
    path('eliminarBeneficiario/<int:id>',beneficiarioviews.eliminarBeneficiario, name="eliminarBeneficiario"),










]


