$(document).ready(function(){
	//Autocomplete OFF
	$('input').attr('autocomplete','off');
	
	//Desaparecer el error list en la validacion de formularios
	$("form input").focus(function() {
		$(this).parent().prev(".errorlist").fadeOut();
	});
});