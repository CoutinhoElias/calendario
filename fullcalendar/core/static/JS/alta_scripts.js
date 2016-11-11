

	jQuery("#id_Colonia").autocomplete({
	source: "/api/get_colonias/",
	minLength: 2,
	});
jQuery(document).ready( function() {
  var now = new Date();
  var month = (now.getMonth() + 1);               
  var day = now.getDate();
  if(month < 10) 
    month = "0" + month;
  if(day < 10) 
    day = "0" + day;
  var today = day + '/' + month + '/' + now.getFullYear() ;
  jQuery('#id_Solicitud').val(today);



  
});

jQuery(function() {

 jQuery('#id_Solicitud').datepicker({ autoSize: true });
 jQuery('#id_formset_sencilla-Solicitud').datepicker({ autoSize: true });

 jQuery(":input").blur(function() {
   if(this.id != 'id_Observaciones') {
     this.value = this.value.toUpperCase();
   }
 });

 jQuery('#id_NumInt').attr('disabled', 'disabled');
 jQuery('input').blur(function () {
   if (jQuery('#id_NumExt').val()) {
     jQuery('#id_NumInt').removeAttr('disabled');
   } else {
     jQuery('#id_NumInt').attr('disabled', 'disabled');
   }
 });
 

   // jQuery('input[type=text]').addClass('form-control');
   // jQuery('select').addClass('form-control');
   // jQuery('select').width('174px');


   

});
