from django.contrib import messages
from django.shortcuts import redirect, render

from Nuevavida.vistas.loginview import encryptPass
from..models import Usuario

def showRestablecer(request):
    return render(request, 'restablecer.html')

def cambiarPassword(request, id):
    context = {"id":id}
    return render(request, 'showRestablecer.html', context)

def cambiarPws(request):
    try :
        if request.method=="POST":
            usuario = Usuario.objects.get(pk = request.POST['id'])
            usuario.password = encryptPass(request.POST['password']) 
            usuario.save()
            messages.success(request,"Cambió de contraseña correctamente!")

        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('Nuevavida:index')

def restablecer(request):
    from django.core.mail import send_mail
    try: 
        if request.method=="POST":
            correoR = request.POST["correo"]
            print(correoR)
            us = Usuario.objects.get(correo = correoR)
            print(us.password)
            send_mail(
                'Mensaje de Funeraria Nueva Vida:',
                'Restablezca su contraseña en el siguiente enlace:\n'+
                'http://127.0.0.1:8000/Nuevavida/restablecerPassword/'+str(us.pk),
                'yazabala38@misena.edu.co',
                [correoR],
                fail_silently=False,
        )
        messages.info(request,'correo enviado')
    except Exception as e: 
        messages.error(request,f"ERROR:{e}")

    return render(request,'index.html')