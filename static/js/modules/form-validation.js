/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

jQuery Validation

Options:

https://jqueryvalidation.org/validate/

*/

import validate from 'jquery-validation';

export function initFormValidation() {
    $('form.validate-form').each(function(){
        // init
        var $form = $(this);
        // init form validation
        var form_to_validate = $form.validate({
            onkeyup: false,
            onfocusout: function(element) {
                // option 1: INSTANT validation after leaving a form field es required
                // this.element(element);
                // option 2: validate on submit
                return false;
            },
            errorPlacement: function(error,element) {
                return false;
            },
            submitHandler: function(form) {
                window.onbeforeunload = null;
                return true;
            }
        });
        // optional: validate on page load by adding a class to the form
        if ($form.hasClass('validate-on-page-load')) {
            $form.validate().form();
        }
    });
}

$(function(){

    // on page load
    initFormValidation();

    // custom event
    $(window).on('initFormValidation', function() {
        initFormValidation();
    });

});
