
from email.policy import HTTP
from multiprocessing import context
from time import strftime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime


# MENSAJES TIPO COOKIES TEMPORALES
from django.contrib import messages

# PARA GESTIONAR ERRORES EN LA BASE DE DATOS
from django.db import IntegrityError

#para accedser a las consultas de base de datos

from..models import Pagos, Factura, Usuario


def index(request):
    return render (request,'index.html')

def listarPagos (request):
    q = Pagos.objects.all() #DICCIONARIO CON LOS DATOS 
    context = {"datos":q}
    return render(request, 'pagos/listarPagos.html',context)

def formularioPagos (request):
    p = Usuario.objects.all()
    context = {"Usuarios": p}
    return render(request, 'pagos/agregarPagos.html',context)


def guardarPagos (request):
    try:
        if request.method=="POST":
            usuario = Usuario.objects.get(pk = request.POST["usuario"])
            print(usuario.idplan.precio)
            print(int(request.POST["cuota"]))
            print(usuario.idplan.precio - int(request.POST["cuota"]))
            usuario.deuda = usuario.idplan.precio - int(request.POST["cuota"])
            usuario.save()
            factura = Factura(
                fechaPago = datetime.datetime.now(),
                totalDeuda = usuario.deuda,
                totalPago = request.POST["cuota"]
            )
            factura.save()
            q = Pagos(
                valor = request.POST["valor"],
                fechaPago = datetime.datetime.now(),
                cedulaUsuario= usuario,
                cuota = request.POST["cuota"],
                idFactura = factura
            )
            q.save()
            messages.success(request," El pago fue guardado correctamente!")
        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarPagos')

        


def buscarUsuario(request):
    print(request.POST["usuario"])
    usuario = Usuario.objects.get(pk = request.POST["usuario"])
    usuario.idplan.precio = usuario.idplan.precio + usuario.deuda
    p = Usuario.objects.all()
    context = {"Usuarios": p ,"Usuario": usuario}
    return render(request, 'pagos/agregarPagos.html',context)
    
