jQuery(document).on('focus', ':input', function() {
    jQuery(this).attr('autocomplete', 'off');
});

jQuery('#notif_btn').click(function() {
    jQuery('#notif_dd').html('&nbsp;').load('/get_notificaciones');
});

jQuery('#toler_btn').click(function() {
    jQuery('#toler_dd').html('&nbsp;').load('/get_tolerancia');
});

jQuery('#proc_btn').click(function() {
    jQuery('#proc_dd').html('&nbsp;').load('/get_proceso');
});

jQuery('.chat_user').click(function($) {

    jQuery.ajax({
            url: "/chat_leido/" + this.id,
            beforeSend: function(xhr) {
                xhr.overrideMimeType("text/plain; charset=x-user-defined");
            }
        })
        .done(function(data) {
            if (console && console.log) {
                console.log("Sample of data:", data.slice(0, 100));
            }
        });

});

jQuery(document).ready(function() {

    jQuery('#id_Solicitud').datepicker({
        autoSize: true
    });
    jQuery('#id_Visita').datepicker({
        autoSize: true
    });
    jQuery('#id_Salida').datepicker({
        autoSize: true
    });
    // Deprecated since Jquery 1.7
    // $(':input[type="text"]').live('focus', function() {
    //     $(this).attr('autocomplete', 'off');
    // });



    jQuery("input[type=submit],button[type=submit], #submit-id-submit").click(function(e) {

        jQuery("input[type=text]").each(function() {
            this.value = this.value.toUpperCase();

            jQuery("input[type=text]").each(function() {
                var self = jQuery(this);
                try {
                    var v = self.autoNumeric('get');
                    self.autoNumeric('destroy');
                    self.val(v);
                } catch (err) {
                }
            });


        });


        jQuery("#id_Valor").autoNumeric('destroy');
        jQuery("#id_formset_sencilla-Valor").autoNumeric('destroy');

    });


    jQuery('#id_Valor').autoNumeric('init', {
        aSign: '$'
    });
    jQuery('#id_formset_sencilla-Valor').autoNumeric('init', {
        aSign: '$'
    });
    jQuery('#id_Gastos').autoNumeric('init', {
        aSign: '$'
    });
    jQuery('#id_Importe').autoNumeric('init', {
        aSign: '$'
    });


    var sidebar_left = jQuery.cookie('sidebar_left');
    if (sidebar_left == 'closed') {
        jQuery("#main-page-container").addClass("sidebar-collapsed");
    } else {
        jQuery("#main-page-container").removeClass("sidebar-collapsed");
    }

});

function printDiv(divName) {
    var divName = document.getElementById(divName);
    var printContents = divName.innerHTML;
    var originalContents = document.body.innerHTML;
    document.body.innerHTML = printContents;
    window.print();
    document.body.innerHTML = originalContents;
}


var opts = {
    "closeButton": true,
    "debug": false,
    "positionClass": "toast-top-right",
    "toastClass": "black",
    "onclick": null,
    "showDuration": "300",
    "hideDuration": "1000",
    "timeOut": "5000",
    "extendedTimeOut": "1000",
    "showEasing": "swing",
    "hideEasing": "linear",
    "showMethod": "fadeIn",
    "hideMethod": "fadeOut"
};

socket.on('on_connect', function(users) {
    // socket connected
    console.log(users);

    for (var x in users) {
        jQuery(".user_" + users[x]).switchClass("is-offline", "is-online", 1000, "easeInOutQuad");
    }


    console.log("Estás conectado");
});


// Recibe evento de proceso
socket.on('message_receive', function(message) {
    console.log(message);
    toastr.success(message.message, '', opts);
    jQuery('#noti_ind').html('&nbsp;').load('/notificaciones_ind')
});

//Recibe evento de chat
socket.on('chat_receive', function(message) {
    console.log(message);
    var sender_name = message.send_user_first_name + " " + message.send_user_last_name;
    toastr.success(message.message, sender_name + " dice: ", opts);
    neonChat.pushMessage(message.send_user_id, message.message.replace(/<.*?>/g, ''), sender_name, new Date(), true, true);
    neonChat.renderMessages(message.send_user_id, false);
});

// Recibe cambio de estatus
socket.on('status_change', function(message) {
    var element = jQuery(".user_" + message.user_id);
    if (message.status == "is-online") {
        element.switchClass("is-offline", "is-online", 1000, "easeInOutQuad");
        //toastr.success("Se ha conectado " + element.text(), '', opts);
        console.log(message.status);
    } else {
        element.switchClass("is-online", "is-offline", 1000, "easeInOutQuad");
        console.log(message.status);
        //toastr.success("Se ha desconectado " + element.text(), '', opts);
    }

});