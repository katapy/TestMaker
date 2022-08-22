/**
 * Modal Window be active.
 * @param {int} id Modal window id.
 */
 let SetModalActive = function(id) {
    item_type = location.pathname.split('/')[2];
    $.ajax({
        type: 'GET',
        url: `/testmaker/${item_type}/modal/${id}`,
        success: function(data) {
            if(id !== 0) {
                AsyncGetItem(item_type, id, item_type).then((item) => {
                    CreateMoodal(data, item, item_type);
                });
            }
            else {
                item = new Item(0, '', '', item_type);
                CreateMoodal(data, item, item_type);
                StartEdit(id);
            }
        }
    });
}

/**
 * Create modal component.
 * @param {string} data origin data
 * @param {Item} item Item
 * @param {string} item_type Item type
 */
let CreateMoodal = function(data, item, item_type) {
    modal_id = "#js-modal-" + item.id
    modal_id += ", #js-overlay";
    modal = data
        .replace(/\$id/g, item.id)
        .replace(/\$name/g, item.name)
        .replace(/\$detail/g, item.detail)
        .replace(/\$item/g, item_type);
    $("#js-overlay").after(modal);
    $(modal_id).addClass("open");
    path = `${location.pathname.replace(item_type, 'usecase')}?${item_type}=${item.id}`;
    frame = CreateIFrame('usecase', path);
    $('#subitem').append(frame);
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
