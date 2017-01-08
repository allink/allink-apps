/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Swiper by iDangero.us

API:

http://idangero.us/swiper/api/

*/

import Swiper from 'swiper';

$(function(){

    function initiSwiperInstances() {

        var swiper_containers = document.querySelectorAll('.swiper-default');

        // loop through instances
        for (var swiper_instance of swiper_containers) {
            // determine number of slides
            var number_of_slides = swiper_instance.querySelectorAll('.swiper-slide').length;
            // no point in initializing swiper if there is only one slide
            if(number_of_slides < 2) {
                swiper_instance.classList.add('swiper-disabled');
                continue;
            }
            // default
            var mySwiper = new Swiper (swiper_instance, {
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

        }

    }

    // on page load
    initiSwiperInstances();

    $(window).on('initiSwiperInstances', function() {
        initiSwiperInstances();
    });

});
