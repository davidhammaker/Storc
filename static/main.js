heights = ['Very short', 'Short', 'Average', 'Tall', 'Very tall'];

weights = ['Underweight', 'Average', 'Overweight'];

hairColors = ['Black', 'Dark brown', 'Brown', 'Light brown', 'Dirty blond', 'Blond', 'Strawberry blond', 'Red', 'Auburn', 'White', 'Silver'];

eyeColors = ['Brown', 'Blue', 'Green', 'Gray', 'Hazel'];

scars = ['Scar over left eye', 'Scar over right eye', 'Scar on nose', 'Scar on upper lip', 'Scar on lower lip', 'Scar on left cheek', 'Scar on right cheek', 'Scar on chin', 'Scar along jawline', 'Scar on forehead'];

uniqueAttributes = ['Flawless complexion', 'Freckled face', 'Much acne', 'Big ears', 'Small ears', 'Big nose', 'Small nose', 'Perfect nose', 'Wide mouth', 'Small mouth', 'Wide eyes', 'Narrow eyes', 'Bushy eyebrows', 'Narrow eyebrows', 'Slight unibrow', 'High cheekbones', 'Square jaw', 'Pointed chin', 'Flat chin', 'Perfect jawline', 'Perfect teeth', 'Crooked teeth', 'Missing one tooth', choice(scars)];

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

    let uniqueAttributeElement = document.getElementById('unique_attribute');
    assignAttribute(uniqueAttributes, uniqueAttributeElement);
};

select();
