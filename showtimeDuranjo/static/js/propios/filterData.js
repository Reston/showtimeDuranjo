$(document).ready(function () {
    $('#menuFiltro li a').click(function(e) {
    e.preventDefault();
    // fetch the class of the clicked item
    var ourFilter = $(this).attr('data-filter');

    // reset the active class on all the buttons
    $('#menuFiltro li').removeClass('active');
    // update the active state on our clicked button
    $(this).parent().addClass('active');

    if(ourFilter == 'all') {
      // show all our items
      $('.lista .wrapper').children('a.itemGaleria').slideDown('slow');
    }
    else {
      // hide all elements that don't share ourFilter
      $('.lista .wrapper').children('a:not(.' + ourFilter + ')').fadeOut('slow');
      // show all elements that do share ourFilter
      $('.lista .wrapper').children('a.' + ourFilter).slideDown('slow');
    }
    return false;
  });
});