function validarPlan(){
    let plan = document.getElementById("cedulaUsuario").value;
    if( plan != 1 ){
       document.getElementById('tipouser').style.display='block';
       console.log(plan)
    }
    else{
        document.getElementById('tipouser').style.display='none';
        document.getElementById('ceduBenefi').style.display='none';
        console.log(plan)
    }
}

function verificar(){
    let benefici = document.getElementById('benefici').checked;
    if( benefici == true){
        document.getElementById('ceduBenefi').style.display='block';
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

