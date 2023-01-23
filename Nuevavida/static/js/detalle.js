function traerBeneficiario(){
    let idUsuario = document.getElementById('idUsuario');
    let idUser = idUsuario.value;
    $.ajax({
        headers: { "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val() },
        url : "../traerBeneficiariosxCotizante/",
        type : 'POST',
        data: {id:idUser},
        dataType:"text", // send as JSON
        success : function(data, textStatus, jqXHR) {
            tblbeneficiario(JSON.parse(data))            
        },
        error: function(jqXHR, textStatus, errorMessage) {
            alert("Error"); // Optional            
        }
    })

}


function tblbeneficiario(beneficiarios){ 
    console.log(beneficiarios.length)
    let tip = document.getElementById('tipo').value;
    console.log(tip)
    let html = "<option value='4'>-----------</option>";
    for(let i = 0; i < beneficiarios.length; i++){
        html += "<option value='"+beneficiarios[i].pk+"'>"+beneficiarios[i].fields["nombreBeneficiario"] + " " + beneficiarios[i].fields["apellidoBeneficiario"]+"</option>";

    }
    $("#idBeneficiario").html(html);
    
}

function selectradio(){
    let radioco = document.getElementById('tipo').checked;
    let barrablock = document.getElementById('cedulaBeneficiario');
    if(radioco == true){
        barrablock.style.display = 'none';
    }
    else{
        barrablock.style.display = 'block';
    }
}

fechaVelacion.min = new Date().toISOString().split("T")[0];
fechaEntierro.min = new Date().toISOString().split("T")[0];

