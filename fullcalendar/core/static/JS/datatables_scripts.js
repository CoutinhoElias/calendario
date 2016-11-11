  jQuery(document).ready(function() {
    

    jQuery('#masiva_button').click(function() {

      // Some code

      if (jQuery(".form-checkbox").is(':checked')) {

        var selected = [];
        jQuery('input:checked').each(function() {
          selected.push(jQuery(this).parent().next().next().next().next().next().next().next().next().html());
        });
        var bandera = true;
        for (var i = 0; i < selected.length; i++) {
          // Logs "try 0", "try 1", ..., "try 4".
          if (selected[0] != selected[i]) {
            bandera = false;
            console.log(selected[i]);
            //console.log( bandera );
          }
        }

        if (bandera == false) {
          sweetAlert("Todos los servicios deben pertenecer a la misma colonia.", "", "warning");
        } else {
          jQuery('#forma_masiva').modal('show');
          // console.log(selected.toString());
        }

        var selected = [];

        // jQuery('#visita_masiva').modal('show');
      } else {
        sweetAlert("Selecciona al menos una casilla.", "", "warning");
      }

    });





  });