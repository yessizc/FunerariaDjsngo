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

from..models import Usuario 


def index(request):
    return render (request,'index.html')

def listarUsuarios (request):
    q = Usuario.objects.all() #DICCIONARIO CON LOS DATOS DE TRABAJADOR
    context = {"datos":q}
    return render(request, 'usuario/listarUsuario.html',context)

def formularioUsuario (request, id):
    print(id)
    if id != 0:
        q = Usuario.objects.get(pk = id) 
        q.fechaNacimiento = q.fechaNacimiento.strftime('%Y-%m-%d')
        print(q.fechaNacimiento)
        context = {"Usuario":q}
        return render(request, 'usuario/agregarUsuario.html',context)
    else:
        t = {'id':id}
        context = {"Usuario":t}
        return render(request,'usuario/agregarUsuario.html', context)


def guardarUsuario (request):
    print(request.POST["telefono"])
    try:
        if request.method=="POST":
            q = Usuario(
                cedula = request.POST["cedula"],
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                telefono = request.POST["telefono"],
                correo = request.POST["correo"],
                fechaNacimiento= datetime.datetime.strptime(request.POST["fechaNacimiento"], "%Y-%m-%d").date()
            )
            q.save()
        #si todo esta bien.
            messages.success(request," El Usuario fue guardado correctamente!")
            #messages.info(request," probando info!")
            #messages.warning(request," probando warning!")
            #messages.debug(request," probando debug")
            #messages.error(request," probando error")
        
        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('usuario:listarUsuario')


def editarUsuario (request, id):
    print("update")
    try :
        if request.method=="POST":

            usuario = Usuario.objects.get(pk = id)
            usuario.cedula = request.POST["cedula"]
            usuario.nombre = request.POST ["nombre"]
            usuario.apellido = request.POST["apellido"]
            usuario.telefono = request.POST["telefono"]
            usuario.correo = request.POST["correo"]
            usuario.fechaNacimiento= datetime.datetime.strptime(request.POST["fechaNacimiento"], "%Y-%m-%d").date()
            usuario.save()
            messages.success(request," El Usuario fue editado correctamente!")

        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarUsuario')


def eliminarUsuario (request, id):
    try:
        usuario = Usuario.objects.get(pk = id)
        usuario.delete()
        messages.success(request," El Usuario se ha eliminado correctamente!")

    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarUsuario')




    
