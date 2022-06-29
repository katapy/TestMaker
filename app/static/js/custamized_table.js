// function addButtonClick(){
$('#btn').click(function(){
    alert('Click');
});

function onChangeNewInput(){
    let element = document.getElementById('newInput');
    data = {"new_input": element.value};
    json = JSON.stringify(data);  // Convert to json.
    $.ajax({
        type: "POST",
        url: "/testmaker/table",
        data: json,
        contentType: "application/json",
        success: function(msg) {
            $('div').html(msg);
            console.log(msg);
        },
        error: function(msg) {
            console.log("error");
        }
    });
}
let create_table = function() {
    data = {"test": "test"};
    json = JSON.stringify(data);  // Convert to json.
    $.ajax({
        type: "POST",
        url: "/testmaker/table",
        data: json,
        contentType: "application/json",
        success: function(msg) {
            $('div').html(msg);
            console.log(msg);
        },
        error: function(msg) {
            console.log("error");
        }
    });
}
$(document).ready(function() {
    create_table();
});