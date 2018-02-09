$(document).ready(function() {
    $('.button-collapse').sideNav();
    $('.slider').slider({
        'height': 500
    });
    $('.dropdown-button').dropdown();
    $('.collapsible').collapsible();

    $('#gallery .gallery_links').simpleLightbox({
        'navText': [
            '<i class="fa fa-angle-left"></i>',
            '<i class="fa fa-angle-right"></i>',
        ]
    });
});
