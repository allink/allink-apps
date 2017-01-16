import { triggerClassOnScroll } from '../../../allink_core_static/js/modules/trigger-class-on-scroll';

$(function(){

    /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    Header

    IMPORTANT: If the 'header buffer' is enabled, the scroll distance breakpoints have to be the same height (AT LEAST), otherwise the buffer becomes visible.

    */

    function initHeader() {

        if (document.querySelector('.site-header.compact-mode-enabled')) {
            var scroll_distance = 70;
            if ($(window).width() >= 768) {
                scroll_distance = 70;
            }
            if ($(window).width() >= 1024) {
                scroll_distance = 125;
            }
            triggerClassOnScroll({
                'scroll': scroll_distance,
                'class_to_trigger': 'compact-mode',
                'element': document.querySelector('.site-header.compact-mode-enabled')
            });
        }

    }

    // on page load
    initHeader();

    // custom event
    $(window).on('initHeader', function() {
        initHeader();
    });

    // initialize again when viewport width has changed
    $(window).on('viewportWidthHasChanged', function(){
        initHeader();
    });

});
