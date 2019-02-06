'use strict';

let hairColors = [
    'Black',
    'Dark brown',
    'Brown',
    'Light brown',
    'Dirty blond',
    'Blond',
    'Strawberry blond',
    'Red',
    'Auburn',
    'White',
    'Silver'
];

let eyeColors = [
    'Brown',
    'Blue',
    'Green',
    'Gray',
    'Hazel'
];

let scars = [
    'Scar over left eye',
    'Scar over right eye',
    'Scar on nose',
    'Scar on upper lip',
    'Scar on lower lip',
    'Scar on left cheek',
    'Scar on right cheek',
    'Scar on chin',
    'Scar along jawline',
    'Scar on forehead'
];

let uniqueAttributes;
function defineUniqueAttributes() {
    uniqueAttributes = [
        'Flawless complexion',
        'Freckled face',
        'Much acne',
        'Big ears',
        'Small ears',
        'Big nose',
        'Small nose',
        'Perfect nose',
        'Wide mouth',
        'Small mouth',
        'Wide eyes',
        'Narrow eyes',
        'Bushy eyebrows',
        'Narrow eyebrows',
        'Slight unibrow',
        'High cheekbones',
        'Square jaw',
        'Pointed chin',
        'Flat chin',
        'Perfect jawline',
        'Perfect teeth',
        'Crooked teeth',
        'Missing one tooth',
        choice(scars)
    ];
};

let colors = [
    'maroon',
    'red',
    'orange',
    'coral',
    'yellow',
    'lime green',
    'green',
    'aqua',
    'light blue',
    'blue',
    'dark blue',
    'purple',
    'violet',
    'black',
    'gray',
    'white',
    'brown'
];

let favoriteClothesGeneric;
let favoriteClothesMale;
let favoriteClothesFemale;
function defineClothes() {
    favoriteClothesGeneric = [
        `${articleChoice(colors)} beanie`,
        `${articleChoice(colors)} baseball cap`,
        `${articleChoice(colors)} scarf`,
        `${articleChoice(colors)} hoodie`,
        `${articleChoice(colors)} jacket`,
        `a leather jacket`,
        `jeans and ${articleChoice(colors)} T-shirt`,
        `shorts and ${articleChoice(colors)} T-shirt`,
        `a sci-fi T-shirt`,
        `a video game T-shirt`,
        `${articleChoice(colors)} cardigan`
    ];
    favoriteClothesMale = [
        `a tuxedo whenever possible`,
        `a suit and tie`,
        `just denim overalls`,
        `a sports jersey`,
        `any shirt and ${articleChoice(colors)} bow tie`,
        `skinny jeans and ${articleChoice(colors)} button-up shirt`,
        `a plaid flannel shirt`
    ];
    favoriteClothesFemale = [
        `${articleChoice(colors)} evening gown`,
        `${articleChoice(colors)} dress`,
        `${articleChoice(colors)} skirt`,
        `${articleChoice(colors)} short skirt`,
        `skinny jeans and ${articleChoice(colors)} T-shirt`,
        `${choice(colors)} yoga pants`,
        `${articleChoice(colors)} blouse`
    ];
};

let mannerisms = [
    'I frequently have one eyebrow raised.',
    'I talk with my hands.',
    'I keep very still. I don\'t move much.',
    'I\'m always tapping my foot or my fingers.',
    'I am very good at keeping eye contact.',
    'I struggle to maintain eye contact.',
    'I\'m always looking around. I\'m easily distracted.',
    'My nose is always turned up.',
    'I find myself looking down a lot.',
    'I have a habit of slouching.',
    'My posture improves when someone is speaking to me.',
    'I snap my fingers to help me remember things.',
    'My face is very expressive.',
    'I\'m always finding something to lean against.',
    'I cross my arms when I talk to someone.',
    'I tend to shove my hands in my pockets.',
    'My eyes drift to the ceiling when I\'m thinking.',
    'I stroke my chin when I\'m being serious.',
    'I hum approvingly while I\'m listening to someone.',
    'Sitting or standing, my legs are almost always crossed.',
    'I\'m always pushing my hair back.',
    'I bite my lip when I\'m concentrating.',
    'If possible, my hands are always folded and my legs are straight.',
    'Eye contact is not my priority. I only look at what I\'m doing.',
    'I wrinkle my nose when I\'m frustrated.',
    'I nod to myself when I have an idea.',
    'I walk in long, slow strides.',
    'I speed-walk everywhere I go.',
    'My face is impossible to read.',
    'I rub my hands together when I\'m exited, or when I have a plan.'
];

let speakingStyles = [
    'I speak very rapidly, but I articulate well.',
    'I talk so fast that I often mix up words.',
    'I studder a bit.',
    'I have trouble finishing a sentence. My voice trails off.',
    'I speak quickly when I get excited or angry.',
    'My words are slow and precise.',
    'I am in no hurry to finish a sentence. I take my time with my words.',
    'I tend to repeat myself. I say the same thing twice.',
    'I take too long to answer a question.',
    'I say only what I have to, and nothing I don\'t.',
    'The pitch of my voice is a rollercoaster, always rising and falling.',
    'My voice can be monotone at times.',
    'I have a dynamic voice. My volume, speed, and tone are always changing.',
    'I mumble the words I really want to say, but everything else is loud and clear.',
    'My voice is soft, even when I want to speak up.',
    'I have no volume control. When I open my mouth, the whole world hears.',
    'I am a brilliant speaker, captivating individuals and crowds.',
    'I am a big fan of one-word replies.',
    'My tone has a calming effect on others.',
    'When I speak, I always sound excited.',
    'My tone has a pensive flavor.',
];

let athletics = [
    'baseball',
    'basketball',
    'football',
    'soccer',
    'bowling',
    'boxing',
    'golf',
    'hockey',
    'tennis',
    'running',
    'fencing',
    'martial arts',
    'acrobatics',
    'swimming'
];
let mediums = [
    'acrylic paint',
    'oil paint',
    'watercolor paint',
    'pencil',
    'colored pencil',
    'crayon',
    'charcoal',
    'pastel',
    'oil pastel',
    'clay',
    'marker'
];
let artisans = [
    'blacksmith',
    'carpenter',
    'glassblower',
    'jeweler',
    'leatherworker'
];
let instruments = [
    'piano',
    'violin',
    'viola',
    'cello',
    'upright bass',
    'bass',
    'guitar',
    'drums',
    'trumpet',
    'french horn',
    'clarinet',
    'flute',
    'tuba',
    'euphonium',
    'saxophone'
];
let writtenWorks = [
    'novels',
    'short stories',
    'flash fiction',
    'poetry',
    'comics',
    'screenplays',
    'plays',
    'musicals',
    'prose',
    'technical papers'
];
let skills;
function defineSkills() {
    skills = [
        `I'm an athlete, and I'm best at ${choice(athletics)}.`,
        `I make great art. My best medium is ${choice(mediums)}.`,
        `I am ${articleChoice(artisans)}, and I do a fine job.`,
        `Music is my specialty. I play the ${choice(instruments)}.`,
        `I am a talented singer.`,
        `I am a gifted writer. I mostly write ${choice(writtenWorks)}.`,
        `I am very persuasive.`,
        `I am very good at mathematics.`,
        `I have read hundreds, if not thousands, of books.`,
        `I'm great with computers.`,
        `I'm a natural leader.`,
        `I have an excellent memory.`,
        `I'm a good liar. I can make anyone believe anything.`
    ];
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
    let gender = document.getElementById('gender').textContent;

    let heightElement = document.getElementById('height');
    let heightRaw;
    if (gender == 'Male') {
        heightRaw = Number.parseInt((Math.random() * 13) + 64);
    }
    else {
        heightRaw = Number.parseInt((Math.random() * 13) + 60);
    }
    let height = `${Number.parseInt(heightRaw / 12)}'${heightRaw % 12}"`
    heightElement.textContent = height;

    let weightElement = document.getElementById('weight');
    let weight;
    function weightChoice(minimum, maximum) {
        return Number.parseInt((Math.random() * (maximum - minimum) + minimum));
    };
    if (heightRaw <= 62) {
        weight = weightChoice(90, 140);
    }
    else if (heightRaw <= 64) {
        weight = weightChoice(95, 150);
    }
    else if (heightRaw <= 66) {
        weight = weightChoice(100, 160);
    }
    else if (heightRaw <= 68) {
        weight = weightChoice(105, 170);
    }
    else if (heightRaw <= 70) {
        weight = weightChoice(110, 180);
    }
    else if (heightRaw <= 72) {
        weight = weightChoice(115, 190);
    }
    else if (heightRaw <= 74) {
        weight = weightChoice(125, 200);
    }
    else {
        weight = weightChoice(130, 210);
    }
    weightElement.textContent = weight + ' lb';

    let hairColorElement = document.getElementById('hair_color');
    assignAttribute(hairColors, hairColorElement);

    let eyeColorElement = document.getElementById('eye_color');
    assignAttribute(eyeColors, eyeColorElement);

    let uniqueAttributeElement = document.getElementById('unique_attribute');
    assignAttribute(uniqueAttributes, uniqueAttributeElement);

    let favoriteClothes = favoriteClothesGeneric;
    if (gender == 'Male') {
        favoriteClothes = favoriteClothes.concat(favoriteClothesMale);
    }
    else {
        favoriteClothes = favoriteClothes.concat(favoriteClothesFemale);
    }

    let favoriteClothesElement = document.getElementById('favorite_clothes');
    assignAttribute(favoriteClothes, favoriteClothesElement);

    let mannerismsOneElement = document.getElementById('mannerism_one');
    let mannerismsTwoElement = document.getElementById('mannerism_two');
    let mannerismOne = choice(mannerisms);
    let mannerismTwo = choice(mannerisms);
    while (mannerismOne == mannerismTwo) {
        mannerismTwo = choice(mannerisms);
    }
    mannerismsOneElement.textContent = mannerismOne;
    mannerismsTwoElement.textContent = mannerismTwo;

    let speakingStyleElement = document.getElementById('speaking_style');
    speakingStyleElement.textContent = choice(speakingStyles);

    let skillElement = document.getElementById('skill');
    skillElement.textContent = choice(skills);
};

function scramble() {
    defineClothes();
    defineUniqueAttributes();
    defineSkills();
    select();
};

scramble();
