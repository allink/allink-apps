/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Video functionality for our "Content Plugin"

*/

// Enable support for iPads
// https://github.com/bfred-it/iphone-inline-video
import makeVideoPlayableInline from 'iphone-inline-video';

$(function() {

    /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    Helper Functions and Events

    */

    $.fn.isOnScreen = function(){

        var element = this.get(0);
        var bounds = element.getBoundingClientRect();

        return bounds.top < window.innerHeight && bounds.bottom > 0;

    };

    $.fn.scrollStopped = function(callback) {

        // init
        var timeout = 30;

        // fire delayed scroll
        $( this ).scroll(function(){
            var self = this, $this = $( self );
            if ( $this.data( 'scrollTimeout' ) ) {
                clearTimeout( $this.data( 'scrollTimeout' ) );
            }
            $this.data( 'scrollTimeout' , setTimeout( callback, timeout, self ) );
        });

    };

    $(window).resize(function() {

        // init
        var timeout = 150;

        if(this.resizeTO) clearTimeout(this.resizeTO);
        this.resizeTO = setTimeout(function() {
            $(this).trigger('resizeEnd');
        }, timeout);

    });

    /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    Handle Video Playback

    */

    function handle_video_playback() {

        // init
        var $videos = $( '.the-video' );
        var loaded_class = 'loaded';
        var on_pause_class = 'on-pause';
        var isIpad = navigator.userAgent.indexOf("iPad") != -1 ;

        // loop through video sections
        $videos.each( function(){

            // init
            var $vid = $( this );

            // first of all, check whether we're on mobile or not
            var show_video = toggle_video_visibility( $vid );

            // in the mobile version the video element is not visible
            if( true === show_video ) {

                // start video when element is on screen
                if( $vid.isOnScreen() ) {

                    // per default, a video is "on pause"
                    if( $vid.hasClass( on_pause_class ) ) {

                        // check load status of video
                        // https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/readyState
                        var video_state = parseInt( $vid.get(0).readyState );
                        if( 0 === video_state ) {
                            $vid.get(0).load();
                        }else if(isIpad === true) {
                            makeVideoPlayableInline($vid.get(0), false /* hasAudio */, false /* false = run everywhere */);
                        }

                        $vid.get(0).play();

                        $vid.parents('.video-container').addClass(loaded_class);
                        $vid.get(0).addEventListener('canplay', function() {
                            $vid.addClass(loaded_class);
                        });

                        setTimeout(function(){

                        },150);

                        // remove class
                        $vid.removeClass( on_pause_class );

                    }

                }
                // not on screen? pause it
                else {

                    // pause the video and..
                    $vid.get(0).pause();

                    // ..add class
                    $vid.addClass( on_pause_class );

                }

            }

        });

    }

    function toggle_video_visibility( $vid ) {

        // init
        var window_width = parseInt( $( window ).width() );
        var min_width_breakpoint = 768;
        var show_video = false;
        var loaded_class = 'loaded';

        // don't re-apply the changes
        if( !$vid.hasClass( loaded_class ) ) {

            // make sure to ONLY load the video when not on mobile
            if( window_width >= min_width_breakpoint ) {

                // set poster
                var poster = $vid.attr( 'data-poster' );
                $vid.attr( 'poster', poster );

                // set video source
                var $source = $vid.find( 'source' );
                var video_source = $source.attr( 'data-src' );
                $source.attr( 'src', video_source );

                // set flag so we won't do it again
                $vid.addClass( loaded_class );

                // set return value
                show_video = true;

            }

        }else {
            show_video = true;
        }

        return show_video;

    }

    // on page load
    handle_video_playback();

    // when scrolling has stopped
    $(window).scrollStopped(function(){
        handle_video_playback();
    });

    // when resizing the window
    $(window).on( 'resizeEnd', function(){
        handle_video_playback();
    });

});
