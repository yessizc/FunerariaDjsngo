from django.shortcuts import render

#Beneficiario
#Index
"""Esta funcion envia al index principal siempre y cuando este logeado por eso solicita permisos
Args:
context:este trae el objeto sesion
permisos:trae el rol

"""

#ListarBeneficiario
"""Esta funcion es la encargada de de listar todos los beneficiarios registrados en el sistema
    Args:
    q:Esta variable trae a todo el objeto beneficiario
    permisos:Esta variable trae el rol
    context:Esta variable trae el objeto sesion
    bf:Esta variable trae el id del usuario para los permisos

"""

#FormularioBeneficiario
"""Esta funcion es la encargada de mostrar el formulario para registrar a un usuario
    Args:
    q:Esta variable trae a todo el objeto beneficiario
    p:Esta variable trae todo el objeto usuario
    permisos:Esta variable trae el rol del usuario
    context:Esta variable trae el objeto sesion

"""

#GuardarBeneficiario
"""Esta funcion es la encargada de guardar los datos del beneficiario enviados por medio del formulario 
    Args:
    q:Esta variable nos guarda los datos que enviamos del formulario

"""

#EditarBeneficiario
"""Esta funcion es la encargada de permitirnos editar los datos del beneficiario
    Args:
    beneficiario:Esta variable es la que trae todos los datos del beneficiario y poder mostrarlos en el formulario

"""

#EliminarBeneficiario
"""Esta funcion es la encargada de permitirnos borrar a un beneficiario
    Args:
    beneficiario:Esta variable es la que trae el objeto beneficiario 

"""

#DetalleFuneral
#Index
"""Esta funcion envia al index principal siempre y cuando este logeado por eso solicita permisos
    Args:
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#listarDetalle
"""Esta funcion es la encargada de listar todos los detalles del funeral que esten en la base de datos
    Args:
    q:Esta variable nos trae todo el objeto DetalleFuneral
    context:Esta variable nos trae el objeto sesion
    permisos:Esta variable trae el rol
    
"""

#formularioDetalle
"""Esta funcion es la encargada de mostrarnos el pormulario para un nuevo ingreso de algun DetalleFuneral
    Args:
    t:Esta variable nos trae solamente el id de el DetalleFuneral
    p:Esta vaiable nos trae a todo el objeto usuario
    q:Esta variable nos trae todo el objeto DetalleFuneral
    context:Esta variable nos trae el objeto sesion
    permisos:Esta variable trae el rol
    
"""

#guardarDetalle
"""Esta funcion es la encargada de dejarnos guardar toda la informacion enviada a traves del formulario
    Args:
    q:Esta variable es la que guarda toda la informacion que manda el formulario y lo guarda en la base de datos
    
"""

#editarDetalle
"""Esta funcion es la encargada de dejarnos editar el DetalleFuneral
    Args:
    detalle:Esta variable nos trae todo el objeto DetalleFuneral y nos permite mostrar los datos registrados en la base de datos
    
"""

#eliminarDetalle
"""Esta funcion es la encargada de permitirnos eliminar un registro de DetalleFuneral
    Args:
    detalle:Esta variable nos trae todo el objeto DetalleFuneral y por medio del id borrar el registro
    
"""

#Factura
#index
"""Esta funcion envia al index principal siempre y cuando este logeado por eso solicita permisos
    Args:
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#listarFactura
"""Esta funcion nos permite listar Todas las facturas guardada en la base de datos
    Args:
    pagos:Esta variable nos trae los pagos registrados con la cedula del usuario
    u:Esta variable nos trae el objeto usuario
    us:Esta variale nos trae la cedula del usuario
    fs:Esta variable nos trae a todo el objeto factura
    q:Esta variable nos trae la lista de lo que se muestra en la factura
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#verFactura
"""Esta funcion nos permite listar Todas las facturas guardada en la base de datos
    Args:
    f:Esta VAriable nos trae el id del objeto factura
    p:Esta variable nos filtra las facturas dependiendo de la cedula del usuario
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#Login
#encryptPass
"""Esta funcion es la encargada de encriptar la clave
    Args:
    password:Nos trae la clave para encriptarla

"""

#login
"""Esta funcion es la encargada de encriptar la clave
    Args:
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol
    usuario:Nos trae el objeto usuario

"""

#Pagos
#index
"""Esta funcion envia al index principal siempre y cuando este logeado por eso solicita permisos
    Args:
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#listarPagos
"""Esta funcion nos permite listar los pagos registrados en la base de datos
    Args:
    us:Nos filtra los pagos dependiendo la cedula del usuario
    q:Nos trae el objeto usuario
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#formularioPagos
"""Esta funcion nos permite mostrar el formulario para registrar un nuevo pago
    Args:
    t:Trae solo el id del objeto plan
    p:Nos trae el objeto usuario
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#guardarPagos
"""Esta funcion nos permite guardar los datos enviados por medio del formulario
    Args:
    factura:Nos trae el objeto factura
    q:Es la que guarda los datos enviados
    usuario:Nos trae el objeto usuario
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#buscarUsuario
"""Esta funcion nos permite buscar el usuario por medio del id
    Args:
    p:Nos trae el objeto usuario
    context:Esta variable este trae el objeto sesion

"""

#Planes
#index
"""Esta funcion envia al index principal siempre y cuando este logeado por eso solicita permisos
    Args:
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#listarPlan
"""Esta funcion se encarga de listarnos todos los planes registrados en la base de datos
    Args:
    q:Nos trae el objeto plan
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#formularioPlan
"""Esta funcion nos permite mostar el formulario para guardar un nuevo plan en la base de datos
    Args:
    t:Nos trae solament el id del objeto plan
    q:Nos trae el objeto plan
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#guardarPlan
"""Esta funcion se encarga de guardar los datos enviados desde el formulario y registrarlos en la base de datos
    Args:
    q:Es la encargada de guardar los datos enviados por medio del formulario

"""

#editarPlan
"""Esta funcion es la que nos permite editar los datos del plan
    Args:
    plan:Nos trae el objeto Plan y nos muestra los datos registrados en el formulario

"""

#eliminarPlan
"""Esta funcion es la que nos permite eliminar un plan de la base de datos
    Args:
    plan:Nos trae el objeto Plan

"""

#Usuario
#index
"""Esta funcion envia al index principal siempre y cuando este logeado por eso solicita permisos
    Args:
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#listarUsuario
"""Esta funcion es la que nos permite listar todos los usuarios registrados en la base de datos
    Args:
    q:Nos trae el objeto usuario
    us:Nos trae solamente el id del usuario
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#formularioUsuario
"""Esta funcion nos permite mostrar el formulario para registrar un nuevo usuario
    Args:
    q:Nos trae el objeto usuario
    p:Nos trae el objeto plan
    t:Nos trae solo el id del usuario
    context:Esta variable este trae el objeto sesion
    permisos:Esta variable trae el rol

"""

#guardarUsuario
"""Esta funcion nos permite guardar los datos enviados por medio del formulario
    Args:
    q:Guarda los datos que llegan por medio del formulario

"""

#editarUsuario
"""Esta funcion nos permite editar a un usuario registrado en la base de datos
    Args:
    usuario:trae el objeto usuario y nos muestra los datos en el formulario para poderlo editar

"""

#eliminarUsuario
"""Esta funcion nos permite eliminar a un usuario de la base de datos
    Args:
    usuario:trae el objeto usuario

"""