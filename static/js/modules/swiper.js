/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Swiper by iDangero.us

API:

http://idangero.us/swiper/api/

*/

import { initiSwiperInstances } from 'allink-core-static/js/modules/swiper';

$(function(){

    var options = {
        // define options here
    };

    // on page load
    initiSwiperInstances(options);

    // custom event
    $(window).on('initiSwiperInstances', function() {
        initiSwiperInstances(options);
    });

});
