/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Mobile Nav Toggle

http://getbootstrap.com/javascript/#collapse

*/

import 'bootstrap/js/collapse';


/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Custom Navigation Dropdown and Tweaks

*/

function initNavigation() {

    /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    Toggle a class when mobile nav is expanded

    */

    $('.navbar-toggle').on('click',function(){
        $('html').toggleClass('nav-expanded')
    });


    /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    Toggle subnav on larger screens

    */

    // STEP 1: click anywhere on the DOM hides all subnavs
    $( document ).on( 'click touchend', function(e){

        // hide only if user has clicked somewhere ELSE but the opened subnav
        if( $(e.target).parents('.nav-dropdown').hasClass('opened') ) {
            // don't do anything
        }else {
            hideExpandedSubnav();
        }

    });

    // STEP 2 (overwrites STEP 1): toggle subnav visibility
    $( '.nav-dropdown > a').on( 'click', function( e ){

        // init
        var $current_subnav = $( this ).siblings( '.subnav' );
        var $overlay = $( '.content-overlay' );
        var visible_class = 'visible';
        var device_width = $( window ).width();
        var min_width_breakpoint = 992; // when is the full menu shown?

        // stops climbing up the DOM, which overwrites STEP 1
        e.stopPropagation();

        // stop following the link
        e.preventDefault();

        // check if current subnav is visible
        var child_is_visible = $current_subnav.hasClass(visible_class);

        // hide all previously opened subnavs
        hideExpandedSubnav();

        // second, display the subnav if it was NOT visible before
        if(child_is_visible) {
            $current_subnav.removeClass(visible_class);
            $current_subnav.parents('.nav-dropdown').removeClass('opened');
            if( device_width >= min_width_breakpoint ) {
                $overlay.removeClass(visible_class);
            }
        }else {
            $current_subnav.addClass(visible_class);
            $current_subnav.parents('.nav-dropdown').addClass('opened');
            if( device_width >= min_width_breakpoint ) {
                $overlay.addClass(visible_class);
            }
        }

    });

    // Optional: Selector of an element that closes the nav
    $( '.subnav-close').on( 'click', function(e){
        e.preventDefault();
        hideExpandedSubnav();
    });

    // Close Subnave when hitting ESC
    $(document).keydown(function(evt) {
        evt = evt || window.event;
        var isEscape = false;
        if ("key" in evt) {
            isEscape = evt.key == "Escape";
        } else {
            isEscape = evt.keyCode == 27;
        }
        if (isEscape) {
            hideExpandedSubnav();
        }
    });

}

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Touch device navigation fixes

*/

function hideExpandedSubnav() {

    // init
    var device_width = $( window ).width();
    var visible_class = 'visible';
    var $overlay = $( '.content-overlay' );
    var min_width_breakpoint = 992; // when is the full menu shown?

    // hide overlay
    $overlay.removeClass(visible_class);

    // only apply on expanded navigation
    if( device_width >= min_width_breakpoint ) {
        $('.subnav').each(function(){
            var $this = $(this);
            if( $this.hasClass(visible_class) ) {
                $this.removeClass(visible_class);
                $this.parents('.nav-dropdown').removeClass('opened');
            }
        });
    }

}

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Init

*/

$(function(){

    // on page load
    initNavigation();

    // custom events
    $(window).on('initNavigation', function() {
        initNavigation();
    });

    $(window).on('hideExpandedSubnav', function() {
        hideExpandedSubnav();
    });

    // initialize again when viewport width has changed
    $(window).on('viewportWidthHasChanged', function(){
        hideExpandedSubnav();
    });

});
