import GalleryGrid from 'gallery-grid';
import { nodeListToArray } from './helper-functions';

let gallery_containers = document.querySelectorAll('.gallery-grid-content-type.gallery');
if(gallery_containers) {
    nodeListToArray(gallery_containers).map((value) => {
        new GalleryGrid(value);
    });
}
