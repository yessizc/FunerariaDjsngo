
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
    context = {}
    if "idUser" in request.session:
        permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
        context = {"sesion" : permisos}
    return render (request,'index.html', context)
    """Esta funcion envia al index principal siempre y cuando este logeado por eso solicita permisos
    Args:
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

    """

def listarPagos (request):
    permisos = {}
    q = None
    if "rol" in request.session:
        if request.session["rol"] == '1':
            q = Pagos.objects.all() #DICCIONARIO CON LOS DATOS 
            for i in q:
                i.valor = '{:,}'.format(i.valor)
                i.cuota = '{:,}'.format(i.cuota)
                i.idFactura.totalDeuda = '{:,}'.format(i.idFactura.totalDeuda)
        else:
            us = Pagos.objects.filter(cedulaUsuario = request.session["idUser"])
            q = [us][0]
            for i in q:
                i.valor = '{:,}'.format(i.valor)
                i.cuota = '{:,}'.format(i.cuota)
                i.idFactura.totalDeuda = '{:,}'.format(i.idFactura.totalDeuda)
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
    else:
        messages.warning(request,"para ingresar debe iniciar sesion...")
        return render (request,'index.html')   
    #print(q[0].idFactura.totalDeuda)     
    context = {"datos":q,"sesion":permisos}
    return render(request, 'pagos/listarPagos.html',context)
    """Esta funcion nos permite listar los pagos registrados en la base de datos
    Args:
    us:Nos filtra los pagos dependiendo la cedula del usuario
    q:Nos trae el objeto usuario
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

    """

def formularioPagos (request):
    permisos = {}
    if "idUser" in request.session:
        permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
        if request.session["rol"]=='1':
            p = Usuario.objects.all()
        else:
            p=Usuario.objects.filter(pk=request.session["idUser"])
        context = {"Usuarios": p, "sesion": permisos}
        return render(request, 'pagos/agregarPagos.html',context)
    else:
        messages.warning(request,"para ingresar debe iniciar sesion...")
        return render (request,'index.html') 
    """Esta funcion nos permite mostrar el formulario para registrar un nuevo pago
    Args:
    t:Trae solo el id del objeto plan
    p:Nos trae el objeto usuario
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

    """


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
    """Esta funcion nos permite guardar los datos enviados por medio del formulario
    Args:
    factura:Nos trae el objeto factura
    q:Es la que guarda los datos enviados
    usuario:Nos trae el objeto usuario
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

    """
        


def buscarUsuario(request):
    permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
    usuario = Usuario.objects.get(pk = request.POST["usuario"])
    usuario.idplan.precio = usuario.idplan.precio + usuario.deuda
    pagos = Pagos.objects.filter(cedulaUsuario = usuario.pk).first()
    fechahoy = str(datetime.date.today().day) + "/" + str(datetime.date.today().month) + "/" + str(datetime.date.today().year)
    if pagos:
        pagos.fechaPago = str(pagos.fechaPago.day) + "/" + str(datetime.date.today().month) + "/" + str(datetime.date.today().year)
    p = Usuario.objects.all()
    context = {"Usuarios": p ,
                "Usuario": usuario , 
                "sesion" : permisos, 
                "pagosInfo" : pagos, 
                "fechaHoy": fechahoy
                }
    return render(request, 'pagos/agregarPagos.html',context)
    """Esta funcion nos permite buscar el usuario por medio del id
    Args:
    p:Nos trae el objeto usuario
    context:Esta variable este trae el objeto sesion

    """
