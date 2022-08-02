
/**
 * create button.
 * @param {string} function_name onclick button function name.
 * @param {string} text button text.
 * @return {string} button.
 */
let CreateButton = function(function_name, text) {
    btn = $('<button />');
    btn.attr('onclick', function_name);
    btn.text(text);
    return btn;
}