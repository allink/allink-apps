import Masonry from 'masonry-layout';
import imagesLoaded from 'imagesloaded';
import { getClosest } from './helper-functions';
import { loadAjaxItems } from './ajax-load-items';

// initialize grid
if(document.querySelector('.grid-dynamic-container')) {
    var grids_on_page = document.querySelectorAll( '.grid-dynamic-container' );

    var MasonryImagesReveal = function(masonry, items) {
        var itemSelector = masonry.options.itemSelector;

        var displayItem = function(index, items) {
            if (items.length <= index) {
                return;
            }

            var item = items[index];

            masonry.element.appendChild(item);
            item.style.opacity = 0;

            if(!item.querySelector('img')) {
                masonry.appended(item);
                item.style.opacity = 1;
                displayItem(index + 1, items);
            }

            // preload img
            else {
                new imagesLoaded(item.querySelector('img'), imgLoad => {
                    // climb up to the closest .grid-item
                    var closest = getClosest( imgLoad.elements[0], '.grid-item' );

                    masonry.appended(item);
                    item.style.opacity =  1;
                    displayItem(index + 1, items);
                });
            }
        };

        displayItem(0, items);

        return this;
    };

    for ( var i = 0, len = grids_on_page.length; i < len; i++ ) {

        // init
        var masonry_grid = grids_on_page[i].querySelector('.the-grid');
        var $content_section = $(masonry_grid).parents('.content-section');

        // instanciate grid
        var masonry_instance = new Masonry(masonry_grid, {
            columnWidth: '.grid-sizer',
            percentagePosition: true,
            // itemSelector: '.' + grid_item_class,
            transitionDuration: '0'
        });

        // handle AJAX requests
        $content_section.find('.ajax-load-items').on('click', function(e){

            // init
            var $trigger = $(this);
            e.preventDefault();

            // Do AJAX stuff
            loadAjaxItems($trigger, masonry_grid, masonry_instance);

        });

        // reveal Masonry Images
        new MasonryImagesReveal(
            masonry_instance,
            grids_on_page[i].querySelectorAll('.grid-items .grid-item')
        );

    }
}
