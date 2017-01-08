/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Parallax

*/

$.fn.parallax = function(extraOptions) {
    var $window = $(window);
    var options = extraOptions || {};
    var $this = $(this);

    var getScrollTop = options.getScrollTop || function(scrollTop, parentTop) {
        return scrollTop - parentTop + $window.height();
    };

    var fadeOutHeader = function($gallery) {
        var $parent = $gallery.parent();
        var height = $gallery.parent().height();
        var difference = $gallery.height() - $parent.height();
        var scrollTop = getScrollTop($window.scrollTop(), $parent.offset().top);
        var scrollProgress = scrollTop / ($window.height() + height);

        if(options.updateCallback) {
            options.updateCallback($gallery, difference, scrollProgress);
        }

        if(options.reversed) {
            $gallery.css('transform', 'translate3d(0, -' + difference * scrollProgress + 'px, 0)')
            .css('-webkit-transform', 'translate3d(0, -' + difference * scrollProgress + 'px, 0)');
        }
        else {
            $gallery.css('transform', 'translate3d(0, ' + (difference * scrollProgress - difference) + 'px, 0)')
            .css('-webkit-transform', 'translate3d(0, ' + (difference * scrollProgress - difference) + 'px, 0)');
        }
    };

    var loopCall = function() {
        $this.each(function(key, value) {
            fadeOutHeader($(value));
        });
    };

    $window.scroll(function() {
        loopCall();
    });

    $window.resize(function() {
        loopCall();
    });

    loopCall();
    setTimeout(function() {
        loopCall();
    }, 10);
};

function initParallax() {
    $('.parallax-enabled .bg-image').parallax();
}

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Init

*/

$(function(){

    // on page load
    initParallax();

    // custom events
    $(window).on('initParallax', function() {
        initParallax();
    });

});
