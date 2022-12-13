
import datetime
from django.contrib import messages
from django.shortcuts import redirect, render

from ..models import DetalleFuneral, Usuario, Beneficiario

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
    """Esta funcion es la encargada de listar todos los detalles del funeral que esten en la base de datos
    Args:
    q:Esta variable nos trae todo el objeto DetalleFuneral
    context:Esta variable nos trae el objeto sesion
    permisos:Esta variable trae el rol
    
    """

def formularioDetalle (request, id):
    permisos = {}
    print(id)
    if id != 0:
        a = DetalleFuneral.objects.get(pk = id)
        q = DetalleFuneral.objects.get(pk = id)
        h = Beneficiario.objects.all()
        p = Usuario.objects.all()
        q.fechaEntierro = q.fechaEntierro.strftime('%Y-%m-%d')
        a.fechaVelacion = q.fechaVelacion.strftime('%Y-%m-%d')
        print(q.fechaEntierro)
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
            context = {"DetalleFuneral":q, "Usuario" : p, "Beneficiario" : h, "sesion" : permisos, "DetalleFuneral":a,}
            return render(request, 'detalle/agregarDetalle.html',context)
        else:
            messages.warning(request,"Solo puede inscribir detalle el administrador")
            return render (request,'index.html') 
    else:
        t = {'id':id}
        h = Beneficiario.objects.all()
        p = Usuario.objects.all()
        if "idUser" in request.session:
            permisos = {"rol" : request.session['rol'], "userId" : request.session['idUser'], "userName" : request.session['userName']}
            context = {"DetalleFuneral":t, "Usuario" : p, "Beneficiario" : h, "sesion" : permisos}
            return render(request,'detalle/agregarDetalle.html', context)
        else:
            messages.warning(request,"Solo puede inscribir detalle el administrador")
            return render (request,'index.html') 
    """Esta funcion es la encargada de mostrarnos el pormulario para un nuevo ingreso de algun DetalleFuneral
    Args:
    t:Esta variable nos trae solamente el id de el DetalleFuneral
    p:Esta vaiable nos trae a todo el objeto usuario
    q:Esta variable nos trae todo el objeto DetalleFuneral
    context:Esta variable nos trae el objeto sesion
    permisos:Esta variable trae el rol
    
    """

def guardarDetalle (request):
    try:
        if request.method=="POST":
            q = DetalleFuneral(
                fechaEntierro = datetime.datetime.strptime(request.POST["fechaEntierro"], "%Y-%m-%d").date(),
                lugarEntierro = request.POST["lugarEntierro"],
                fechaVelacion = datetime.datetime.strptime(request.POST["fechaVelacion"], "%Y-%m-%d").date(),
                lugarVelacion = request.POST["lugarVelacion"],
                idbeneficiario = Beneficiario.objects.get(pk = request.POST["idbeneficiario"]),
                cedulaUsuario = Usuario.objects.get(pk = request.POST["cedulaUsuario"])
            
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
        messages.error(request,f"errorperr: {e}")
           
    return redirect('Nuevavida:listarDetalle')
    """Esta funcion es la encargada de dejarnos guardar toda la informacion enviada a traves del formulario
    Args:
    q:Esta variable es la que guarda toda la informacion que manda el formulario y lo guarda en la base de datos
    
    """


def editarDetalle (request, id):
    try :
        if request.method=="POST":
            detalle = DetalleFuneral.objects.get(pk = id)

            detalle.fechaEntierro = datetime.datetime.strptime(request.POST["fechaEntierro"], "%Y-%m-%d").date()
            detalle.lugarEntierro = request.POST["lugarEntierro"]
            detalle.fechaVelacion = datetime.datetime.strptime(request.POST["fechaVelacion"], "%Y-%m-%d").date()
            detalle.lugarVelacion = request.POST ["lugarVelacion"]
            detalle.cedulaUsuario = Usuario.objects.get(pk = request.POST["cedulaUsuario"])
            detalle.idbeneficiario = Beneficiario.objects.get(pk = request.POST["idbeneficiario"])
            detalle.save()
            messages.success(request," Los datos fueron editados correctamente!")

        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarDetalle')
    """Esta funcion es la encargada de dejarnos editar el DetalleFuneral
    Args:
    detalle:Esta variable nos trae todo el objeto DetalleFuneral y nos permite mostrar los datos registrados en la base de datos
    
    """

def eliminarDetalle (request, id):
    try:
        detalleFuneral = DetalleFuneral.objects.get(pk = id)
        detalleFuneral.delete()
        messages.success(request," La informacion se ha eliminado correctamente!")

    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:listarDetalle')
    """Esta funcion es la encargada de permitirnos eliminar un registro de DetalleFuneral
    Args:
    detalle:Esta variable nos trae todo el objeto DetalleFuneral y por medio del id borrar el registro
    
    """