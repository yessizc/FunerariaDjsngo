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
    let beneficiario = document.getElementById('beneficiario').checked;
    if( beneficiario == true){
        document.getElementById('ceduBenefi').style.display='block';
    }
    else{
        document.getElementById('ceduBenefi').style.display='none';

    }
 
}

function validarBeneficiario(){
    let cedubene = document.getElementById("cedulaBeneficiario").value;
    console.log(cedubene)
}
