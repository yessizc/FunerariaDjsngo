function validarCedula(){
    var cedu = document.getElementById("idUsuario").value;
    const cedula = Usuario.cedula;

    for (cedu; cedu < cedula.lenght; cedu ++){
        if(cedu != cedula)
            alert("Este documento no se encuentra");
            document.getElementById("idUsuario").value = 0;
    }
}