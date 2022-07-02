
/**
 * OnClick btn.
*/
$('#btn').click(function(){
    alert('Click');
});

$(document).ready(function() {
    create_table('{}');
});

/** 
 * On change new input.
*/
function onChangeNewInput(){
    let element = document.getElementById('newInput');
    data = {"new_input": element.value};
    json = JSON.stringify(data);  // Convert to json.
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
    console.log("data: " + data);
    var usage_arr = JSON.parse(data);
    $.each(usage_arr,function(i,rowdata){
        var id = rowdata.id;
        var name = rowdata.name;
        var tr = $('<tr />');
        var id_cell = $('<td />').text(id);
        var name_cell = $('<td />').text(name);
        tr.append(id_cell);
        tr.append(name_cell);
        $('#custamized-table-body').append(tr);   
    });

    var tr = $('<tr />');
    var id = $('<td />').text('');
    var name = $('<td />');
    name.append('<input id="newInput" type="text" name="intput" onchange="onChangeNewInput()">');
    tr.append(id);
    tr.append(name);
    $('#custamized-table-body').append(tr);   
}
