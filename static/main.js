genders = ['Male', 'Female'];

heights = ['Very short', 'Short', 'Average', 'Tall', 'Very tall'];

weights = ['Underweight', 'Average', 'Overweight'];

hairColors = ['Black', 'Dark brown', 'Brown', 'Light brown', 'Dirty blond', 'Blond', 'Strawberry blond', 'Red', 'Auburn', 'White', 'Silver'];

eyeColors = ['Brown', 'Blue', 'Green', 'Gray', 'Hazel'];

function assignAttribute(attributeList, attributeElement) {
    let attribute = attributeList[Number.parseInt((Math.random() * attributeList.length))];
    attributeElement.textContent = attribute;
};

function select() {
    let genderElement = document.getElementById('gender');
    assignAttribute(genders, genderElement);

    let heightElement = document.getElementById('height');
    assignAttribute(heights, heightElement);

    let weightElement = document.getElementById('weight');
    assignAttribute(weights, weightElement);

    let hairColorElement = document.getElementById('hair_color');
    assignAttribute(hairColors, hairColorElement);

    let eyeColorElement = document.getElementById('eye_color');
    assignAttribute(eyeColors, eyeColorElement);
};

select();
