
from email.policy import HTTP
from multiprocessing import context
from time import strftime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# MENSAJES TIPO COOKIES TEMPORALES
from django.contrib import messages

# PARA GESTIONAR ERRORES EN LA BASE DE DATOS
from django.db import IntegrityError

#para accedser a las consultas de base de datos

from..models import MetodoPago


def index(request):
    return render (request,'index.html')

def listarMetodoPago (request):
    q = MetodoPago.objects.all() #DICCIONARIO CON LOS DATOS DE TRABAJADOR
    context = {"datos":q}
    return render(request, 'metodoPago/listarMetodopago.html',context)

def formularioMetodoPago (request, id):
    print(id)
    if id != 0:
        q = MetodoPago.objects.get(pk = id)
        context = {"MetodoPago":q}
        return render(request, 'metodoPago/agregarMetodopago.html',context)
    else:
        t = {'id':id}
        context = {"MetodoPago":t}
        return render(request,'metodoPago/agregarMetodopago.html', context)


def guardarMetodoPago (request):
    try:
        if request.method=="POST":
            q = MetodoPago(
                nombremetodopago= request.POST["nombreMetodo"],
                
                
                
            )
            q.save()
        #si todo esta bien.
            messages.success(request," El metodo de pago fue guardado correctamente!")
            #messages.info(request," probando info!")
            #messages.warning(request," probando warning!")
            #messages.debug(request," probando debug")
            #messages.error(request," probando error")
        
        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarMetodoPago')


def editarMetodoPago (request, id):
    print("update")
    try :
        if request.method=="POST":
            metodoPago = MetodoPago.objects.get(pk = id)

            
            metodoPago.nombreMetodo = request.POST["nombreMetodo"]
            
            
            metodoPago.save()
            messages.success(request," El metodo de pago fue editado correctamente!")

        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarMetodoPago')


def eliminarMetodoPago (request, id):
    try:
        metodoPago = MetodoPago.objects.get(pk = id)
        metodoPago.delete()
        messages.success(request," El metodo de pago se ha eliminado correctamente!")

    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarMetodoPago')


