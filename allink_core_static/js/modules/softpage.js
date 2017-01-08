/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

SoftPage AJAX Trigger

Important: The

*/

import SoftPage from 'softpage';
import { node_list_to_array } from './helper-functions';

$(function(){

    const soft_page = new SoftPage({
        onPageLoaded: function(obj) {
            // scroll to top when a softpage has been loaded
            document.querySelector('.tingle-modal').scrollTop = 0;
            // do stuff slighty delayed, so we get all the information we need
            setTimeout(function(){
                // init page meta
                var modal_url = obj.modal.modal.baseURI;
                var modal_page_title_element = obj.modal.modalBoxContent.querySelector('#softpage-page-title');
                var modal_page_title = '';
                // Info for developer, that #softpage-page-title is missing on the detail page
                if (modal_page_title_element != null) {
                    var modal_page_title = modal_page_title_element.textContent;
                }else {
                    console.warn('Softpage is missing #softpage-page-title.');
                }
                // Google Tag Manager
                if (typeof dataLayer !== 'undefined') {
                    dataLayer.push({
                        'event': 'VirtualPageview',
                        'virtualPageURL': modal_url,
                        'virtualPageTitle': modal_page_title,
                    });
                }
                // trigger custom events
                $(window).trigger('initFormModalTrigger');
                $(window).trigger('initOnScreen');
                $(window).trigger('initiSwiperInstances');
            },50);
        }
    });

    function initSoftpageTrigger() {
        node_list_to_array(document.querySelectorAll('[data-trigger-softpage] a')).map((value) => {
            value.addEventListener('click', (event) => {
                event.preventDefault();
                soft_page.loadPage(event.currentTarget.href, true);
            });
        });
    }

    // on page load
    initSoftpageTrigger();

    $(window).on('initSoftpageTrigger', function() {
        initSoftpageTrigger();
    });

});
