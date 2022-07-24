
/**
 * OnClick btn.
*/
$('#btn').click(function(){
    alert('Click');
});

/**
 * Run on ready.
 */
$(document).ready(function() {
    create_data_table('{}');
});

/** 
 * On change new input.
*/
function onChangeNewInput(){
    let element = document.getElementById('newInput');
    data = {"new_input": element.value};
    json = JSON.stringify(data);  // Convert to json.
    create_data_table(json);
}

/** 
 * On change input id.
*/
function onChangeInput(id){
    let element = document.getElementById('input_' + id);
    data = { [id] : element.value};
    json = JSON.stringify(data);  // Convert to json.
    create_data_table(json);

    SetModalActive();
}

/**
 * Create table by data.
 * @param {string} json input data.
 */
function create_data_table(json) {
    $.ajax({
        type: "POST",
        url: location.pathname,
        data: json,
        contentType: "application/json",
        success: function(data) {
            console.log(data);
            create_table(data);
        },
        error: function(msg) {
            console.log(msg);
        }
    });
}

/**
 * Create table by data.
 * @param {string} data Json data which written in table. 
 */
let create_table = function(data) {
    $("#custamized-table-body").empty();
    $("#custamized-table-header").empty();
    var usage_arr = JSON.parse(data);
    var before = usage_arr['before'];
    var header_arr = usage_arr['header'];
    var data_arr = usage_arr['data'];
    var modals = usage_arr['modals'];

    // Set before table
    $('#custam-table').before(before);

    // Set header.
    var header_tr = $('<tr />');
    for(var key in header_arr) {
        var th = $('<th />').text(header_arr[key]);
        header_tr.append(th);
    }
    $('#custamized-table-header').append(header_tr);

    // Set data.
    $.each(data_arr,function(i,rowdata){
        var tr = $('<tr />');
        for(var key in header_arr) {
            var td = $('<td />').append(rowdata[key]);
            tr.append(td);
        }
        $('#custamized-table-body').append(tr);   
    });

    // Set input field
    var tr = $('<tr />');
    var id = $('<td />').text('');
    var name = $('<td />');
    name.append('<input id="newInput" type="text" name="intput" onchange="onChangeNewInput()">');
    tr.append(id);
    tr.append(name);
    $('#custamized-table-body').append(tr);

    // Set modals.
    $.each(modals,function(i,modal){
        $("#js-overlay").after(modal);
    });
}

/**
 * @param {string} path
 */
let Redirect = function(redirect_url) {
    location = redirect_url
}

/**
 * Modal Window be active.
 * @param {int} id Modal window id.
 */
let SetModalActive = function(id) {
    // Open modal window.
    modal_id = "#js-modal-" + id
    modal_id += ", #js-overlay";
    $(modal_id).addClass("open");

    // Close modal window when on click.
    close_id = "#js-close-" + id; 
    $(close_id).on('click', function () { 
        modal.removeClass("open");
    });
}
