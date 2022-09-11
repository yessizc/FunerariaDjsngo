
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
    return render (request,'index.html')

def listarPlan (request):
    q = Plan.objects.all() #DICCIONARIO CON LOS DATOS DE TRABAJADOR
    context = {"datos":q}
    return render(request, 'planes/listarPlan.html',context)

def formularioPlan (request, id):
    print(id)
    if id != 0:
        q = Plan.objects.get(pk = id) 
        q.fechaNacimiento = q.fechaNacimiento.strftime('%Y-%m-%d')
        print(q.fechaNacimiento)
        context = {"Plan":q}
        return render(request, 'Plan/agregarPlan.html',context)
    else:
        t = {'id':id}
        context = {"Plan":t}
        return render(request,'Plan/agregarPlan.html', context)


def guardarPlan (request):
    print(request.POST["telefono"])
    try:
        if request.method=="POST":
            q = Plan(
                nombreplan = request.POST["nombrePlan"],
                precio = request.POST["precio"],
                
                
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
           
    return redirect('usuario:listarPlan')


def editarPlan (request, id):
    print("update")
    try :
        if request.method=="POST":
            plan = Plan.objects.get(pk = id)

            
            plan.nombrePlan = request.POST["nombrePlan"]
            plan.precio = request.POST ["precio"]
            
            plan.save()
            messages.success(request," El Plan fue editado correctamente!")

        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarPlan')


def eliminarPlan (request, id):
    try:
        plan = Plan.objects.get(pk = id)
        plan.delete()
        messages.success(request," El plan se ha eliminado correctamente!")

    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarPlan')




    
