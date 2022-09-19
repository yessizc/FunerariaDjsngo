function validarPlan(){
    var plan = document.getElementById("idCotizante").selectedOptions[0].innerText;
    plan = plan.split(":")[1];
    if(plan == "Individual"){
        alert("No puede agregar beneficiarios a un plan Individual");
        document.getElementById("idCotizante").value = 0;
    }
}