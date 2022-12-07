import datetime
from email.policy import HTTP
import hashlib
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

from..models import Usuario, Plan

def encryptPass(password):
    password = password.encode('utf-8')
    return hashlib.sha512(password).hexdigest()

def index(request):
    context = {}
    if "idUser" in request.session:
        permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser']}
        context = {"sesion" : permisos}
    return render (request,'index.html', context)
    """Esta funcion envia al index principal siempre y cuando este logeado por eso solicita permisos
    Args:
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

    """

def listarUsuario (request):
    permisos = {}
    q = None
    if "rol" in request.session:
        if request.session["rol"] == '1':
            q = Usuario.objects.all()
        else:
            us = Usuario.objects.get(pk = request.session["idUser"])
            q = [us]
        
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']} 
        context = {"datos":q, "sesion":permisos}
        return render(request, 'usuario/listarUsuario.html',context)
    else:
        messages.warning(request,"para ingresar debe iniciar sesion...")
        return render (request,'index.html')
    """Esta funcion es la que nos permite listar todos los usuarios registrados en la base de datos
    Args:
    q:Nos trae el objeto usuario
    us:Nos trae solamente el id del usuario
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

    """

def formularioUsuario (request, id):
    permisos = {}
    print(id)
    if id != 0:
        q = Usuario.objects.get(pk = id) 
        p = Plan.objects.all()
        q.fechaNacimiento = q.fechaNacimiento.strftime('%Y-%m-%d')
        print(q.fechaNacimiento)
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
            context = {"Usuario":q, "Planes" : p, "sesion" : permisos}
            return render(request, 'usuario/agregarUsuario.html',context)
        else:
            messages.warning(request,"para ingresar debe iniciar sesion...")
            return render (request,'index.html') 
    else:
        t = {'id':id}
        p = Plan.objects.all()
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
            context = {"Usuario":t, "Planes" : p, "sesion" : permisos}
            return render(request,'usuario/agregarUsuario.html', context)
        else:
            messages.warning(request,"para ingresar debe iniciar sesion...")
            return render (request,'index.html') 
    """Esta funcion nos permite mostrar el formulario para registrar un nuevo usuario
    Args:
    q:Nos trae el objeto usuario
    p:Nos trae el objeto plan
    t:Nos trae solo el id del usuario
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

    """

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
                password = encryptPass(request.POST['password']),
                idplan = Plan.objects.get(pk = request.POST["idPlan"]),
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
           
    return redirect('Nuevavida:listarUsuario')
    """Esta funcion nos permite guardar los datos enviados por medio del formulario
    Args:
    q:Guarda los datos que llegan por medio del formulario

    """

def editarUsuario (request, id):
    print(request.POST["idPlan"])
    try :
        if request.method=="POST":

            usuario = Usuario.objects.get(pk = id)
            usuario.cedula = request.POST["cedula"]
            usuario.nombre = request.POST ["nombre"]
            usuario.apellido = request.POST["apellido"]
            usuario.telefono = request.POST["telefono"]
            usuario.correo = request.POST["correo"]
            usuario.idplan = Plan.objects.get(pk = request.POST["idPlan"])
            usuario.password = encryptPass(request.POST['password']) 
            usuario.fechaNacimiento= datetime.datetime.strptime(request.POST["fechaNacimiento"], "%Y-%m-%d").date()
            usuario.save()
            messages.success(request," El Usuario fue editado correctamente!")

        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarUsuario')
    """Esta funcion nos permite editar a un usuario registrado en la base de datos
    Args:
    usuario:trae el objeto usuario y nos muestra los datos en el formulario para poderlo editar

    """

def eliminarUsuario (request, id):
    try:
        usuario = Usuario.objects.get(pk = id)
        usuario.delete()
        messages.success(request," El Usuario se ha eliminado correctamente!")

    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarUsuario')
    """Esta funcion nos permite eliminar a un usuario de la base de datos
    Args:
    usuario:trae el objeto usuario

    """



    
