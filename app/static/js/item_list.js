
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
    console.log(data_arr);
    $.each(data_arr,function(i,rowdata){
        var tr = $('<tr />');
        var id = rowdata['id'];
        var name = rowdata['name'];
        var td_id = $('<td />');
        td_id.append('<p>' + id + '</p>');
        var td_name = $('<td />');
       td_name.append(CreateButton(`SetModalActive(${id})`, name));
        tr.append(td_id);
        tr.append(td_name);
        $('#custamized-table-body').append(tr);   
    });
    
    // Set modals.
    $.each(modals,function(i,modal){
        $("#js-overlay").after(modal);
    });
}

/**
 * Redirect path
 * @param {string} redirect_url
 */
let Redirect = function(redirect_url) {
    location = redirect_url
}