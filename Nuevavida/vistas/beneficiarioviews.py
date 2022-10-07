
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

from..models import Beneficiario, Usuario


def index(request):
    return render (request,'index.html')

def listarBeneficiario (request):
    q = Beneficiario.objects.all() #DICCIONARIO CON LOS DATOS 
    context = {"datos":q}
    return render(request, 'beneficiario/listarBeneficiario.html',context)

def formularioBeneficiario (request, id):
    print(id)
    if id != 0:
        q = Beneficiario.objects.get(pk = id) 
        p = Usuario.objects.all()
        q.fechaNacimiento = q.fechaNacimiento.strftime('%Y-%m-%d')
        context = {"Beneficiario":q, "Usuario": p}
        return render(request, 'beneficiario/agregarBeneficiario.html',context)
    else:
        t = {'id':id}
        p = Usuario.objects.all()
        context = {"Beneficiario":t, "Usuario": p}
        return render(request,'beneficiario/agregarBeneficiario.html', context)


def guardarBeneficiario (request):
    try:
        if request.method=="POST":
            q = Beneficiario(
                cedulaBeneficiario = request.POST["cedulaBeneficiario"],
                nombreBeneficiario = request.POST["nombreBeneficiario"],
                apellidoBeneficiario = request.POST["apellidoBeneficiario"],
                fechaNacimiento = datetime.datetime.strptime(request.POST["fechaNacimiento"],"%Y-%m-%d").date(),
                cedulaUsuario = Usuario.objects.get(pk = request.POST["idUsuario"]),
                
                
            )
            q.save()
        #si todo esta bien.
            messages.success(request," El beneficiario fue guardado correctamente!")
            #messages.info(request," probando info!")
            #messages.warning(request," probando warning!")
            #messages.debug(request," probando debug")
            #messages.error(request," probando error")
        
        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarBeneficiario')


def editarBeneficiario (request, id):
    print(request.POST["idUsuario"])
    try :
        if request.method=="POST":
            beneficiario =Beneficiario.objects.get(pk = id)

            beneficiario.cedulaBeneficiario = request.POST["cedulaBeneficiario"]
            beneficiario.nombreBeneficiario = request.POST["nombreBeneficiario"]
            beneficiario.apellidoBeneficiario = request.POST["apellidoBeneficiario"]
            beneficiario.fechaNacimiento = datetime.datetime.strptime(request.POST["fechaNacimiento"],"%Y-%m-%d").date()
            beneficiario.cedulaUsuario= Usuario.objects.get(pk = request.POST["idUsuario"])
            
            beneficiario.save()
            messages.success(request," El beneficiario fue editado correctamente!")

        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarBeneficiario')


def eliminarBeneficiario (request, id):
    try:
        beneficiario = Beneficiario.objects.get(pk = id)
        beneficiario.delete()
        messages.success(request," El beneficiario se ha eliminado correctamente!")

    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarBeneficiario')




    
