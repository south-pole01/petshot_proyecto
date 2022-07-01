$("#formulario1").validate({
    rules:{
        "txtEmail":{
            required: true,
            email: true
        },
        "txtContrasenia": {
            required: true,
            minlength: 5
        },

        "txtRepetirContra": {
            required: true,
            equalTo: '#id_txtContrasenia'
                    }

    },

    messages: {
        "txtEmail": {
            required: 'Ingrese mail!!',
            email: 'No cumple formato'
        },
        "txtContrasenia":{
            required: 'Ingresa la contrasenia!!',
            minlength: 'Mínimo 5 caracteres'
        },
        "txtRepetirContra": {
            required: 'Repita el Password!!',
            equalTo: 'Deben ser iguales'
                    }        

    }
})

jQuery(document).ready(function () {
    $("#vercontra").on('click', function () {
 
        var pass = $("#id_txtContrasenia");
        var pass2 = $("#id_txtRepetirContra");
 
        var fieldtype = pass.attr('type');
        var fieldtype2 = pass2.attr('type');
 
        if (fieldtype == 'password' & fieldtype2 == 'password') {
            pass.attr('type', 'text');
            pass2.attr('type', 'text');
            $(this).text("Ocultar contrasenia");
        } else {
            pass.attr('type', 'password');
            pass2.attr('type', 'password');
            $(this).text("Ver Contrasenia");
        }
 
    });
 
});