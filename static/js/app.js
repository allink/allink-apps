/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Essentals

*/

import $ from 'jquery';


/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

NPM Packages

*/

import 'lazysizes';


/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

allink CORE (NPM package)

===

These modules provide core functionality.

Note: Should you need a customzied project specific version of one of
the following modules:

Head over to the 'allink-core-static' repo, comment out the module below,
download the latest version and place it in the ./modules folder.

*/

import 'allink-core-static/js/modules/ajax-form';
import 'allink-core-static/js/modules/bootstrap-select';
import 'allink-core-static/js/modules/btn-ajax-loader';
import 'allink-core-static/js/modules/datepicker';
import 'allink-core-static/js/modules/djangocms-tweaks';
import 'allink-core-static/js/modules/form';
import 'allink-core-static/js/modules/form-validation';
import 'allink-core-static/js/modules/full-height';
import 'allink-core-static/js/modules/masonry';
import 'allink-core-static/js/modules/seo';
import 'allink-core-static/js/modules/site-overlay';
import 'allink-core-static/js/modules/softpage';
import 'allink-core-static/js/modules/table';
import 'allink-core-static/js/modules/tingle';
import 'allink-core-static/js/modules/video';
import 'allink-core-static/js/modules/viewport-dimensions';

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Custom Scripts

*/

import './modules/ajax-load-items';
import './modules/header';
import './modules/map';
import './modules/navigation';
import './modules/onscreen';
import './modules/parallax';
import './modules/swiper';
import './modules/to-the-top';


// TBD: Improve and customize https://github.com/allink/carousel-widget
// import './modules/gallery-grid';


$(function() {

    /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    Legacy: Calls functions which are added to window.onDocumentReady

    Do we need that?

    */

    // function callFnQueue() {
    //     if (window.onDocumentReady) {
    //         if (typeof(window.onDocumentReady) == 'function') {
    //             window.onDocumentReady($);
    //         } else if (typeof(window.onDocumentReady) == 'object') {
    //             for (var i = 0; i < window.onDocumentReady.length; i++) {
    //                 var func = window.onDocumentReady[i];
    //                 if (typeof(func) == 'function') {
    //                     func($);
    //                 }
    //             }
    //         }
    //     }
    // }

});
