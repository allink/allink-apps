import { initParallax } from 'allink-core-static/js/modules/parallax';

$(function(){

    var options = {
        // optional
    };

    // on page load
    initParallax(options);

    // custom event
    $(window).on('initParallax', function(options) {
        initParallax(options);
    });

});
