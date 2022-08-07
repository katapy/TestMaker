/**
 * Modal Window be active.
 * @param {int} id Modal window id.
 */
 let SetModalActive = function(id) {
    item_type = location.pathname.split('/')[2];
    // Open modal window.
    modal_id = "#js-modal-" + id
    modal_id += ", #js-overlay";
    $(modal_id).addClass("open");
    $.ajax({
        type: 'GET',
        url: `/testmaker/${item_type}/modal/${id}`,
        success: function(data) {
            modal = undefined;
            if(id !== 0) {
                AsyncGetItem(item_type, id).then((item) => {
                    modal = data
                        .replace(/\$id/g, item.id)
                        .replace(/\$name/g, item.name)
                        .replace(/\$detail/g, item.detail)
                        .replace(/\$item/g, item_type);
                        $("#js-overlay").after(modal);
                        $(modal_id).addClass("open");
                });
            }
            else {
                modal = data
                    .replace(/\$id/g, 0)
                    .replace(/\$name/g, '')
                    .replace(/\$detail/g, '')
                    .replace(/\$item/g, item_type);
                $("#js-overlay").after(modal);
                $(modal_id).addClass("open");
                // Start edit if create new.
                StartEdit(id);
            }
        }
    })
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
