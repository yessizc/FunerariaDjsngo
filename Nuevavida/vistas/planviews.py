
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

from..models import Plan 


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

def listarPlan (request):
    permisos = {}
    if "idUser" in request.session:
        permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
        q = Plan.objects.all() #DICCIONARIO CON LOS DATOS DE TRABAJADOR
        context = {"datos":q, "sesion":permisos}
        if  request.session['rol'] == "1":
            return render(request, 'planes/listarPlan.html',context)
        else:
            messages.warning(request,"USTED NO TIENE PERMISOS PARA ACCEDER A ESTE MODULO")
            return render (request,'index.html', context) 
    else:
        messages.warning(request,"para ingresar debe iniciar sesion...")
        return render (request,'index.html') 
    """Esta funcion se encarga de listarnos todos los planes registrados en la base de datos
    Args:
    q:Nos trae el objeto plan
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

    """

def formularioPlan (request, id):
    permisos = {}
    if "idUser" in request.session:
        permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
        if id != 0:
            q = Plan.objects.get(pk = id) 
            context = {"Plan":q, "sesion":permisos}
            return render(request, 'planes/agregarPlan.html',context)
        else:
            t = {'id':id}
            if "idUser" in request.session:
                permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
            context = {"Plan":t, "sesion":permisos}
            return render(request,'planes/agregarPlan.html', context)
    else:
        messages.warning(request,"para ingresar debe iniciar sesion...")
        return render (request,'index.html') 
    """Esta funcion nos permite mostar el formulario para guardar un nuevo plan en la base de datos
    Args:
    t:Nos trae solament el id del objeto plan
    q:Nos trae el objeto plan
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

    """

def guardarPlan (request):
    try:
        if request.method=="POST":
            q = Plan(
                nombrePlan = request.POST["nombre"],
                precio = request.POST["precio"],
                caracteristicas = request.POST["caracteristicas"]
                
            )
            q.save()
        #si todo esta bien.
            messages.success(request," El plan fue guardado correctamente!")
            #messages.info(request," probando info!")
            #messages.warning(request," probando warning!")
            #messages.debug(request," probando debug")
            #messages.error(request," probando error")
        
        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarPlan')
    """Esta funcion se encarga de guardar los datos enviados desde el formulario y registrarlos en la base de datos
    Args:
    q:Es la encargada de guardar los datos enviados por medio del formulario

    """

def editarPlan (request, id):
    print("update")
    try :
        if request.method=="POST":
            plan = Plan.objects.get(pk = id)

            plan.caracteristicas = request.POST["caracteristicas"]
            plan.nombrePlan = request.POST["nombre"]
            plan.precio = request.POST ["precio"]
            
            plan.save()
            messages.success(request," El Plan fue editado correctamente!")

        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarPlan')
    """Esta funcion es la que nos permite editar los datos del plan
    Args:
    plan:Nos trae el objeto Plan y nos muestra los datos registrados en el formulario

    """

def eliminarPlan (request, id):
    try:
        plan = Plan.objects.get(pk = id)
        plan.delete()
        messages.success(request," El plan se ha eliminado correctamente!")

    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarPlan')
    """Esta funcion es la que nos permite eliminar un plan de la base de datos
    Args:
    plan:Nos trae el objeto Plan

    """



    
