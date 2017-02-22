/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

OnScreen - Does stuff when an element is on screen.

https://github.com/silvestreh/onScreen

*/

import OnScreen from 'onscreen';

export function initOnScreen() {

    // when to reveal item: tolerance breakpoints
    let tolerance = 50;
    if ($(window).width() >= 768) {
        tolerance = 100;
    }
    if ($(window).width() >= 1024) {
        tolerance = 200;
    }

    const os = new OnScreen({
        tolerance: tolerance, // options.tolerance is the number of pixels an element is allowed to enter its container boundaries before calling its callback. Defaults to 0.
        debounce: 100, // options.debounce is the number of milliseconds to wait before calling an element's callback after the user has stopped scrolling. Defaults to 100.
        container: window // options.container is the container of the elements you want to track. It accepts a string representing a CSS selector or an HTMLElement object. Defaults to window.
    });

    // Do something when an element enters the viewport
    os.on('enter', '[data-scroll-spy]', (element) => {
        // makes's the element's text red
        element.classList.add('element-visible');
    });
}

$(function(){

    // on page load
    initOnScreen();

    // custom event
    $(window).on('initOnScreen', function() {
        initOnScreen();
    });

});
