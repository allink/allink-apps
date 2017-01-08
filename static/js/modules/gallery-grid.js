import GalleryGrid from 'gallery-grid';
import { node_list_to_array } from './helper-functions';

let gallery_containers = document.querySelectorAll('.gallery-grid-content-type.gallery');
if(gallery_containers) {
    node_list_to_array(gallery_containers).map((value) => {
        new GalleryGrid(value);
    });
}
