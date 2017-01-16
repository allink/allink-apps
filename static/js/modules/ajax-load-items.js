import { initAjaxLoadItemsTrigger } from '../../../allink_core_static/js/modules/ajax-load-items';
import { initMasonry } from '../../../allink_core_static/js/modules/masonry';

$(function(){

    var options = {
        ajax_load_transition_duration: 100,
    };

    // init modules
    initAjaxLoadItemsTrigger(options);
    initMasonry(options);

});
