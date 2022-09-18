import datetime
from email.policy import HTTP
from multiprocessing import context
from time import strftime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.dateparse import parse_datetime

# MENSAJES TIPO COOKIES TEMPORALES
from django.contrib import messages

# PARA GESTIONAR ERRORES EN LA BASE DE DATOS
from django.db import IntegrityError

#para accedser a las consultas de base de datos

from..models import Cotizante, Plan


def index(request):
    return render (request,'index.html')

def listarCotizante (request):
    q = Cotizante.objects.all() #DICCIONARIO CON LOS DATOS DE TRABAJADOR
    context = {"datos":q}
    return render(request, 'cotizante/listarCotizante.html',context)

def formularioCotizante (request, id):
    print(id)
    if id != 0:
        q = Cotizante.objects.get(pk = id) 
        p = Plan.objects.all()
        q.fechaNacimiento = q.fechaNacimiento.strftime('%Y-%m-%d')
        print(q.fechaNacimiento)
        context = {"Cotizante":q, "Planes" : p}
        return render(request, 'cotizante/agregarCotizante.html',context)
    else:
        t = {'id':id}
        p = Plan.objects.all()
        context = {"Cotizante":t, "Planes" : p}
        return render(request,'cotizante/agregarCotizante.html', context)


def guardarCotizante (request):
    print(request.POST["telefono"])
    try:
        if request.method=="POST":
            q = Cotizante(
                cedula = request.POST["cedula"],
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                telefono = request.POST["telefono"],
                correo = request.POST["correo"],
                idplan = Plan.objects.get(pk = request.POST["idPlan"]),
                fechaNacimiento= datetime.datetime.strptime(request.POST["fechaNacimiento"], "%Y-%m-%d").date()
            )
            q.save()
        #si todo esta bien.
            messages.success(request," El Cotizante fue guardado correctamente!")
            #messages.info(request," probando info!")
            #messages.warning(request," probando warning!")
            #messages.debug(request," probando debug")
            #messages.error(request," probando error")
        
        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarCotizante')


def editarCotizante (request, id):
    print(request.POST["idPlan"])
    try :
        if request.method=="POST":

            cotizante = Cotizante.objects.get(pk = id)
            cotizante.cedula = request.POST["cedula"]
            cotizante.nombre = request.POST ["nombre"]
            cotizante.apellido = request.POST["apellido"]
            cotizante.telefono = request.POST["telefono"]
            cotizante.correo = request.POST["correo"]
            cotizante.idplan = Plan.objects.get(pk = request.POST["idPlan"])
            cotizante.fechaNacimiento= datetime.datetime.strptime(request.POST["fechaNacimiento"], "%Y-%m-%d").date()
            cotizante.save()
            messages.success(request," El Cotizante fue editado correctamente!")

        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarCotizante')


def eliminarCotizante (request, id):
    try:
        cotizante = Cotizante.objects.get(pk = id)
        cotizante.delete()
        messages.success(request," El Cotizante se ha eliminado correctamente!")

    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarCotizante')




    
