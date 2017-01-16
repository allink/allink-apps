/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Essentals

*/

import $ from 'jquery';
import feature from 'feature';


/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

NPM Packages

*/

import 'lazysizes';


/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

allink CORE (NPM package)

===

These modules provide core functionality.

Note: Should you need a customzied project specific version of one of
the following modules, head over to the 'allink_core_static' repo,
download the latest version and place it in the  ./modules folder.

*/

import '../../allink_core_static/js/modules/bootstrap-select';
import '../../allink_core_static/js/modules/btn-ajax-loader';
import '../../allink_core_static/js/modules/datepicker';
import '../../allink_core_static/js/modules/djangocms-tweaks';
import '../../allink_core_static/js/modules/form';
import '../../allink_core_static/js/modules/form-modal';
import '../../allink_core_static/js/modules/full-height';
import '../../allink_core_static/js/modules/mailchimp';
import '../../allink_core_static/js/modules/masonry';
import '../../allink_core_static/js/modules/site-overlay';
import '../../allink_core_static/js/modules/softpage';
import '../../allink_core_static/js/modules/table';
import '../../allink_core_static/js/modules/tingle';
import '../../allink_core_static/js/modules/video';
import '../../allink_core_static/js/modules/viewport-dimensions';

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Custom Scripts

*/

import './modules/seo';
import './modules/ajax-load-items';
import './modules/form-validation';
import './modules/parallax';
import './modules/header';
import './modules/map';
import './modules/navigation';
import './modules/onscreen';
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
