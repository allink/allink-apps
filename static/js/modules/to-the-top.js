/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Scrolls to the top of the page

*/

import { triggerClassOnScroll } from '../../../allink_core_static/js/modules/trigger-class-on-scroll';

$(function(){

    /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    To the top!

    */

    if (document.querySelector('.to-the-top')) {
        var scroll_distance = 70;
        if ($(window).width() >= 768) {
            scroll_distance = 70;
        }
        if ($(window).width() >= 1024) {
            scroll_distance = 125;
        }
        triggerClassOnScroll({
            'scroll': scroll_distance,
            'class_to_trigger': 'visible',
            'element': document.querySelector('.to-the-top')
        });
    }

    $('.to-the-top').on('click',function(e){
        var $this = $(this);
        e.preventDefault();
        var target = $this.attr('href');
        window.location = target;
    });

});
