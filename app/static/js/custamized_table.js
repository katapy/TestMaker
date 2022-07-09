
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
 * Create table by data.
 * @param {string} json input data.
 */
function create_data_table(json) {
    $.ajax({
        type: "POST",
        url: "/testmaker/table",
        data: json,
        contentType: "application/json",
        success: function(data) {
            console.log(data);
            create_table(data);
        },
        error: function(msg) {
            console.log("error");
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
    console.log("data: " + data);
    var usage_arr = JSON.parse(data);
    var header_arr = usage_arr['header'];
    var data_arr = usage_arr['data'];

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
            var th = $('<td />').text(rowdata[key]);
            tr.append(th);
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
}
