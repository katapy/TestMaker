
/**
 * Item
 */
class Item {
    /**
     * Item constractor
     * @param {int} id 
     * @param {string} name 
     * @param {string} detail 
     */
    constructor(id, name, detail) {
        this.id = id;
        this.name = name;
        this.detail = detail;
    }
}

/**
 * Perspective
 */
class Perspective extends Item {
    
}

/**
 * Convert json to item.
 * @param {string} json_data json item data
 * @returns Item
 */
let CreateItem = function(json_data) {
    var arr = JSON.parse(json_data);
    return new Item(arr['id'], arr['item_name'], arr['detail'])
}

/**
 * [Async function] Get item by server. 
 * @param {string} type Item type.
 * @param {int} id Item id
 * @returns Item
 */
let AsyncGetItem = function(type, id) {
    return new Promise((resolve, reject) => {
        $.ajax({
            type: 'POST',
            url: `/testmaker/${type}/modal/${id}`,
            async: true,
        }).then(
            function (result) {
                resolve(CreateItem(result));
            },
            function () {
                // Error
                reject();
            })
        }
    )
}
