from ast import Pass
from email.policy import HTTP
from multiprocessing import context
from time import strftime
from typing import List
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime


# MENSAJES TIPO COOKIES TEMPORALES
from django.contrib import messages

# PARA GESTIONAR ERRORES EN LA BASE DE DATOS
from django.db import IntegrityError

#para accedser a las consultas de base de datos

from..models import Cotizante, Factura, Pagos


def index(request):
    return render (request,'index.html')

def listarFactura (request):
    q = Factura.objects.all() #DICCIONARIO CON LOS DATOS 
    context = {"datos":q}
    return render(request, 'factura/listarFactura.html',context)
    

def verFactura (request, id):
    f = Factura.objects.get(pk = id)
    p = list(Pagos.objects.filter(idFactura = id).values('cedulaCotizante'))
    c = Cotizante.objects.get(pk = p[0]["cedulaCotizante"])
    context = {"Factura":f, "Pago" : p, "Cotizante" : c}
    return render(request, 'factura/verFactura.html',context)

def verFacturaPago(request, id):
    p = Pagos.objects.get(pk = id)
    f = Factura.objects.get(pk = p.idFactura.id)
    c = Cotizante.objects.get(pk = p.cedulaCotizante.id)
    context = {"Factura":f, "Pago" : p, "Cotizante" : c}
    return render(request, 'factura/verFactura.html',context)


def descargarFactura(request, id):
    pass

