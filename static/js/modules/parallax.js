import { initParallax } from '../../../allink_core_static/js/modules/parallax';

$(function(){

    var options = {
        selector: '.parallax-enabled .bg-image',
        // updateCallback: function($gallery, difference, scrollProgress){},
        // reversed: false, // boolean
    };

    // init modules
    initParallax(options);

});
