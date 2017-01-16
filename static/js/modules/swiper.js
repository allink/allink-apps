/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Swiper by iDangero.us

API:

http://idangero.us/swiper/api/

*/

import Swiper from 'swiper';

function initiSwiperInstances() {

    // loop through instances
    $('.swiper-container').each(function(i) {
        // init
        var $swiper_instance = $(this);
        // determine number of slides
        var number_of_slides = $swiper_instance.find('.swiper-slide').length;
        // no point in initializing swiper if there is only one slide
        if(number_of_slides < 2) {
            $swiper_instance.addClass('swiper-disabled');
            return true;
        }
        // default
        var mySwiper = new Swiper ($swiper_instance, {
            // global settings
            effect: 'fade',
            speed: 1000, // Number: Duration of transition between slides (in ms)
            autoplay: 3000, // Number: Delay between transitions (in ms). If this parameter is not specified, auto play will be disabled
            slidesPerView: 'auto',
            spaceBetween: 30,
            direction: 'horizontal',
            loop: true, // important: Set to 'false' when scrollbar is enabled
            grabCursor: true,

            // If we need pagination
            pagination: '.swiper-pagination',
            paginationElement: 'span',
            paginationClickable: true,

            // Navigation arrows
            nextButton: '.swiper-button-next',
            prevButton: '.swiper-button-prev',
        });

    });

}

$(function(){

    // on page load
    initiSwiperInstances();

    $(window).on('initiSwiperInstances', function() {
        initiSwiperInstances();
    });

});
