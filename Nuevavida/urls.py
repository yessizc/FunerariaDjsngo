from django.urls import path

from Nuevavida.vistas import planviews

from .vistas import usuarioviews, planviews
 
app_name= "Nuevavida"
urlpatterns = [
    path('', usuarioviews.index,name="index"), 

    # crud usuarios
    
    path('Usuario/',usuarioviews.listarUsuarios, name="listarUsuario"),
    path('editarUsuario/<int:id>',usuarioviews.editarUsuario, name="editarUsuario"),
    path ('formularioUsuario/<int:id>',usuarioviews.formularioUsuario, name="formularioUsuario"),
    path ('agregarUsuario/',usuarioviews.guardarUsuario, name="agregarUsuario"),
    path('eliminarUsuario/<int:id>',usuarioviews.eliminarUsuario, name="eliminarUsuario"),


    # crud Plan

    path('listarPlan/',planviews.listarPlan, name="listarPlan"),
    path('editarPlan/<int:id>',planviews.editarPlan, name="editarPlan"),
    path ('formularioPlan/<int:id>',planviews.formularioPlan, name="formularioPlan"),
    path ('guardarPlan/',planviews.guardarPlan, name="guardarPlan"),
    path('eliminarPlan/<int:id>',planviews.eliminarPlan, name="eliminarPlan"),


    #crud metodos de pago

    #path('MetodoPago/',usuarioviews.listarMetodoPago, name="agregarMetodoPago"),
    #path('MetodoPago/',usuarioviews.listarTrabajador, name="editarMetodoPago"),
    #path ('formularioMetodoPago/<int:id>',views.formulariMetodoPago, name="formularioMetodoPago"),
    #path ('guardarMetodoPago/',views.guardarMetodoPago, name="guardaroPlan"),
    #path('eliminarMetodoPago/<int:id>',usuarioviews.eliminarMetodoPago, name="eliminarMetodoPago"),


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


