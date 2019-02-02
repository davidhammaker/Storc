heights = ['Very short', 'Short', 'Average', 'Tall', 'Very tall'];

weights = ['Underweight', 'Average', 'Overweight'];

hairColors = ['Black', 'Dark brown', 'Brown', 'Light brown', 'Dirty blond', 'Blond', 'Strawberry blond', 'Red', 'Auburn', 'White', 'Silver'];

eyeColors = ['Brown', 'Blue', 'Green', 'Gray', 'Hazel'];

function choice(list) {
    let selection = list[Number.parseInt((Math.random() * list.length))];
    return selection;
};

function assignAttribute(attributeList, attributeElement) {
    let attribute = choice(attributeList);
    attributeElement.textContent = attribute;
};

function select() {
    let heightElement = document.getElementById('height');
    assignAttribute(heights, heightElement);

    let weightElement = document.getElementById('weight');
    weightElement.textContent = Number.parseInt((Math.random() * 100) + 100) + ' lb';

    let hairColorElement = document.getElementById('hair_color');
    assignAttribute(hairColors, hairColorElement);

    let eyeColorElement = document.getElementById('eye_color');
    assignAttribute(eyeColors, eyeColorElement);
};

select();
