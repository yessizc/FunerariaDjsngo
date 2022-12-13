function validarPlan(){
    let ceduben = document.getElementById('ceduBenefi').style.display='block';
    let users = document.getElementById('tipouser').style.display='none';
    let plan = document.getElementById("cedulaUsuario").value;
    if( plan != 1 ){
        users = document.getElementById('tipouser').style.display='block';
        console.log(plan)
       
    }
    else{
        users = document.getElementById('tipouser').style.display='none';
        ceduben = document.getElementById('ceduBenefi').style.display='none';
        idbeneficiario = document.getElementById('idbeneficiario').value = 4;
        console.log(plan)
    }
}

function verificar(){
    let benefici = document.getElementById('benefici').checked;
    if( benefici == true){
        document.getElementById('ceduBenefi').style.display='block';
        console.log(benefici)
    }
    else{
        document.getElementById('ceduBenefi').style.display='none';

    }
 
}
function vamos(){
    let plan = document.getElementById("idbeneficiario").value;
    if( plan != 0 ){
       console.log(plan)
    }
}

fechaVelacion.min = new Date().toISOString().split("T")[0];
fechaEntierro.min = new Date().toISOString().split("T")[0];

