/**
 * Modal Window be active.
 * @param {int} id Modal window id.
 */
 let SetModalActive = function(id) {
    // Open modal window.
    modal_id = "#js-modal-" + id
    modal_id += ", #js-overlay";
    $(modal_id).addClass("open");

    // Start edit if create new.
    if(id === 0) {
        StartEdit(id);
    }
}

/**
 * Start edit modal window
 * @param {int} id Modal window id.
 */
let StartEdit = function(id) {
    edit_item_class = ".edit-item-" + id;
    edit_button_id = "#js-edit-" + id;

    $( edit_item_class ).each( function (){
        $(this).attr('readonly',false);
   } );
   $(edit_button_id).attr('hidden', true);
}
