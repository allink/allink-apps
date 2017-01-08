/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

Tingle.js Tweaks

*/

$(function(){

    /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    Modify Tingle Close Button

    */

    function initTingleModifications() {
        // Update button text (accessibility) and wrap with <span>
        var btn = document.querySelector('.tingle-modal__close');
        var btn_text_wrapper = document.createElement('span');
        btn_text_wrapper.setAttribute('lang', 'en');
        // set button text
        btn.textContent = '';
        btn_text_wrapper.textContent = 'Close';
        btn.append(btn_text_wrapper);
    }

    // on page load, but delayed
    setTimeout(function(){
      initTingleModifications();
    },150);

});
