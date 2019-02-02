'use strict';

let hairColors = ['Black', 'Dark brown', 'Brown', 'Light brown', 'Dirty blond', 'Blond', 'Strawberry blond', 'Red', 'Auburn', 'White', 'Silver'];

let eyeColors = ['Brown', 'Blue', 'Green', 'Gray', 'Hazel'];

let scars = ['Scar over left eye', 'Scar over right eye', 'Scar on nose', 'Scar on upper lip', 'Scar on lower lip', 'Scar on left cheek', 'Scar on right cheek', 'Scar on chin', 'Scar along jawline', 'Scar on forehead'];

let uniqueAttributes;
function defineUniqueAttributes() {
    uniqueAttributes = ['Flawless complexion', 'Freckled face', 'Much acne', 'Big ears', 'Small ears', 'Big nose', 'Small nose', 'Perfect nose', 'Wide mouth', 'Small mouth', 'Wide eyes', 'Narrow eyes', 'Bushy eyebrows', 'Narrow eyebrows', 'Slight unibrow', 'High cheekbones', 'Square jaw', 'Pointed chin', 'Flat chin', 'Perfect jawline', 'Perfect teeth', 'Crooked teeth', 'Missing one tooth', choice(scars)];
};

let colors = ['maroon', 'red', 'orange', 'coral', 'yellow', 'lime green', 'green', 'aqua', 'light blue', 'blue', 'dark blue', 'purple', 'violet', 'black', 'gray', 'white', 'brown'];

let favoriteClothesGeneric;
function defineClothes() {
    favoriteClothesGeneric = [`${articleChoice(colors)} beanie`, `${articleChoice(colors)} baseball cap`, `${articleChoice(colors)} scarf`, `${articleChoice(colors)} hoodie`, `${articleChoice(colors)} jacket`, `a leather jacket`, `jeans and ${articleChoice(colors)} T-shirt`, `shorts and ${articleChoice(colors)} T-shirt`];
};

function choice(list) {
    let selection = list[Number.parseInt((Math.random() * list.length))];
    return selection;
};

function articleChoice(list) {
    let selection = list[Number.parseInt((Math.random() * list.length))];
    let letter = selection[0];
    if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u') {
        selection = 'an ' + selection;
    }
    else {
        selection = 'a ' + selection;
    }
    return selection;
}

function assignAttribute(attributeList, attributeElement) {
    let attribute = choice(attributeList);
    attributeElement.textContent = attribute;
};

function select() {
    let heightElement = document.getElementById('height');
    let heightRaw = Number.parseInt((Math.random() * 17) + 60);
    let height = `${Number.parseInt(heightRaw / 12)}'${heightRaw % 12}"`
    heightElement.textContent = height;

    let weightElement = document.getElementById('weight');
    let weight;
    function weightChoice(minimum, maximum) {
        return Number.parseInt((Math.random() * (maximum - minimum) + minimum));
    };
    if (heightRaw <= 62) {
        weight = weightChoice(100, 150);
    }
    else if (heightRaw <= 64) {
        weight = weightChoice(100, 160);
    }
    else if (heightRaw <= 66) {
        weight = weightChoice(110, 170);
    }
    else if (heightRaw <= 68) {
        weight = weightChoice(115, 180);
    }
    else if (heightRaw <= 70) {
        weight = weightChoice(120, 190);
    }
    else if (heightRaw <= 72) {
        weight = weightChoice(125, 200);
    }
    else if (heightRaw <= 74) {
        weight = weightChoice(135, 210);
    }
    else {
        weight = weightChoice(140, 220);
    }
    weightElement.textContent = weight + ' lb';

    let hairColorElement = document.getElementById('hair_color');
    assignAttribute(hairColors, hairColorElement);

    let eyeColorElement = document.getElementById('eye_color');
    assignAttribute(eyeColors, eyeColorElement);

    let uniqueAttributeElement = document.getElementById('unique_attribute');
    assignAttribute(uniqueAttributes, uniqueAttributeElement);

    let favoriteClothesElement = document.getElementById('favorite_clothes');
    assignAttribute(favoriteClothesGeneric, favoriteClothesElement);
};

function scramble() {
    defineClothes();
    defineUniqueAttributes();
    select();
};

scramble();
