$( document ).ready(function() {
// This is a functions that scrolls to #{blah}link
	$("nav > ul > li").click(function(e){
	// Prevent a page reload when a link is pressed
		e.preventDefault();
	// Call the scroll function
		goToByScroll($(this).attr("id"));

	});

	function goToByScroll(id){
	// Remove "link" from the ID
	console.log(id);
		id = id.replace("Menu", "");
	// Scroll
		$('html,body').animate({
			scrollTop: $("#"+id).offset().top},
			'slow');
	}

});