
import datetime
from django.contrib import messages
from django.shortcuts import redirect, render
from Nuevavida.models import DetalleFuneral, Usuario

def index(request):
    context = {}
    if "idUser" in request.session:
        permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
        context = {"sesion" : permisos}
    return render (request,'index.html', context)

def listarDetalle (request):
    permisos = {}
    q = None
    if "rol" in request.session:
        if request.session["rol"] == '1':
            q = DetalleFuneral.objects.all()
        else:
            de = DetalleFuneral.objects.get(pk = request.session["idDetalle"])
            q = [de]
        
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']} 
        context = {"datos":q, "sesion":permisos}
        return render(request, 'detalle/listarDetalle.html',context)
    else:
        messages.warning(request,"Solo puede inscribir detalle el administrador")
        return render (request,'index.html')

def formularioDetalle (request, id):
    permisos = {}
    print(id)
    if id != 0:
        q = DetalleFuneral.objects.get(pk = id)
        p = Usuario.objects.all()
        q.fechaEntierro = q.fechaEntierro.strftime('%Y-%m-%d')
        print(q.fechaEntierro)
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
            context = {"DetalleFuneral":q, "Usuario" : p, "sesion" : permisos }
            return render(request, 'detalle/agregarDetalle.html',context)
        else:
            messages.warning(request,"Solo puede inscribir detalle el administrador")
            return render (request,'index.html') 
    else:
        t = {'id':id}
        p = Usuario.objects.all()
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
            context = {"DetalleFuneral":t, "Usuario" : p, "sesion" : permisos}
            return render(request,'detalle/agregarDetalle.html', context)
        else:
            messages.warning(request,"Solo puede inscribir detalle el administrador")
            return render (request,'index.html') 


def guardarDetalle (request):
    try:
        if request.method=="POST":
            q = DetalleFuneral(
                nombreDifunto = request.POST["nombreDifunto"],
                cedulaDifunto = request.POST["cedulaDifunto"],
                fechaEntierro = datetime.datetime.strptime(request.POST["fechaEntierro"], "%Y-%m-%d").date(),
                lugarEntierro = request.POST["lugarEntierro"],
                fechaVelacion = datetime.datetime.strptime(request.POST["fechaVelacion"], "%Y-%m-%d").date(),
                lugarVelacion = request.POST["lugarVelacion"],
                cedulaUsuario = Usuario.objects.get(pk = request.POST["cedulaUsuario"]),
                tipoUsuario = request.POST["tipoUsuario"]

            )
            
            q.save()
        #si todo esta bien.
            messages.success(request," Los datos fueron guardados correctamente!")
            #messages.info(request," probando info!")
            #messages.warning(request," probando warning!")
            #messages.debug(request," probando debug")
            #messages.error(request," probando error")
        
        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarDetalle')


def editarDetalle (request, id):
    print(request.POST["cedulaUsuario"])
    try :
        if request.method=="POST":

            detalle = DetalleFuneral.objects.get(pk = id)
            detalle.nombreDifunto = request.POST["nombreDifunto"],
            detalle.cedulaDifunto = request.POST ["cedulaDifunto"],
            detalle.fechaEntierro = datetime.datetime.strptime(request.POST["fechaEntierro"], "%Y-%m-%d").date(),
            detalle.lugarEntierro = request.POST["lugarEntierro"],
            detalle.fechaVelacion = datetime.datetime.strptime(request.POST["fechaVelacion"], "%Y-%m-%d").date(),
            detalle.lugarVelacion = request.POST ["lugarVelacion"],
            detalle.cedulaUsuario = Usuario.objects.get(pk = request.POST["cedulaUsuario"]),
            detalle.save()
            messages.success(request," Los datos fueron editados correctamente!")

        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarDetalle')


def eliminarDetalle (request, id):
    try:
        detalleFuneral = DetalleFuneral.objects.get(pk = id)
        detalleFuneral.delete()
        messages.success(request," La informacion se ha eliminado correctamente!")

    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarDetalle')