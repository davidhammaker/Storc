'use strict';

// Define functions that assist with attribute definition and selection

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
};

/* Define attributes (hairColor, eyeColor, uniqueAttributes and their
subcategories, etc.) */

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
        `I'm a good liar. I can make anyone believe anything.`,
        `I am a brilliant speaker, captivating individuals and crowds.`
    ];
};

let disabilities = [
    'blind',
    'deaf',
    'a cripple',
    'missing an eye',
    'missing an arm',
    'missing a leg'
];
let flaws;
function defineFlaws() {
    flaws = [
        'I have a bad temper. The smallest thing can anger me.',
        'I won\'t turn down a challenge, even if I know I should.',
        'I can\'t walk away from a fight.',
        'I go out of my way to prove I\'m better than my rivals.',
        'I am easily manipulated, even when I\'m aware of others\' intentions.',
        'I have a hard time standing up for myself.',
        'I\'m always telling lies. Sometimes I lie for no reason.',
        'I trust no one. Anyone might let me down.',
        'I have a habit of intentionally irritating people.',
        'I use humor at very innappropriate times.',
        'No matter what anyone tells me, I feel insignificant.',
        'I am envious, always wanting whatever I can\'t have.',
        'I look down on others. Why live in denial of my own superiority?',
        'I use other people, even hurt them, if I have something to gain.',
        'I lie awake plotting ways to spite my rivals.',
        'I defy all forms of authority. No one holds power over me.',
        'Rumors and gossip are my weapons of choice.',
        'I turn close friends against each other if it serves my purpose.',
        'I struggle with an addiction.',
        `I'm ${choice(disabilities)}.`,
        'I have a hard time finding my voice.',
        'I\'m scarred by something that happened to me in my past.',
        'I will always carry the burden of a terrible mistake.',
        'I firmly believe that everyone is hiding something from me.',
        'Money is the only true form of safety and security.',
        'I love my material possessions more than anything.',
        'I sometimes take things that don\'t belong to me.',
        'I have a very low opinion of myself.',
        'I tend to dwell on every little mistake I make.',
        'I am unreliable. No one can depend on me.'
    ];
};

let maleHair = [
    'shaved off',
    'neatly cut short',
    'military cut',
    'crew cut',
    'short and unkempt',
    'long and disheveled',
    'long, but neat',
    'styled with product',
    'slicked back'
];
let femaleHair = [
    'short',
    'shoulder-length, straight',
    'long, straight',
    'very long, straight',
    'shoulder-length, wavy',
    'long, wavy',
    'very long, wavy',
    'shoulder-length, curly',
    'long, curly',
    'very long, curly',
    'shoulder-length, unkempt',
    'long, unkempt',
    'very long, unkempt',
    'long, tied back',
    'very long, tied back',
    'long, braided',
    'very long, braided'
];

let scaryCritters = [
    'spiders',
    'snakes',
    'dogs',
    'cats',
    'birds',
    'bees',
    'frogs',
    'sharks',
    'cockroaches',
    'rodents',
    'bats',
    'ants',
    'all insects'
];
let fears;
function defineFears() {
    fears = [
        `I am terrified of ${choice(scaryCritters)}.`,
        `I stay away from sick people.`,
        `I hate tight spaces, even elevators.`,
        `I panic when I'm in a crowd.`,
        `Thunder storms are my worst nightmare.`,
        `I stay away from water. I'm afraid of drowning.`,
        `I'm deathly afraid of heights.`,
        `I hate doctors and hospitals.`,
        `Keep the light on. I'm afraid of the dark.`,
        `I'm scared that I'll be left behind or forgotten.`,
        `I'm afraid to risk falling in love.`,
        `I shy of camera lenses.`,
        `I get really bad stage-fright.`,
        `Above all, I'm afraid of dying.`
    ];
};

let favoriteThings = [
    'I love winning a game or a competition.',
    'I enjoy learning something new and interesting.',
    'A great book is all I need to have a good time.',
    'Good food always brings me cheer.',
    'I adore all cute animals.',
    'I love a good thrill, especially if it\'s dangerous.',
    'I feel great after completing a hard task.',
    'When I help others, my life has meaning.',
    'Great stories are what I live for.',
    'I\'m always up for a good movie.',
    'I sleep better when I know that justice has been served.',
    'My favorite music always brightens my spirits.',
    'Fine art is a priceless treasure in my eyes.',
    'A great play can really inspire me.',
    'I\'m happiest when I\'m enjoying the sunshine.',
    'Rainfall may make others sad, but I\'ve always liked it.',
    'To me, there\'s nothing like a peaceful snowfall.',
    'I have a special appreciation for wildlife.',
    'The latest and greatest technologies have my attention.',
    'Old-fashioned traditions and objects are precious to me.',
    'There\'s nothing like a comfortable piece of clothing.'
];

// Define an array of mutually exclusive attributes

let exclusions = [
    [
        [
            'I keep very still. I don\'t move much.',
            'If possible, my hands are always folded and my legs are straight.'
        ],
        [
            'I talk with my hands.',
            'I\'m always tapping my foot or my fingers.',
            'I\'m always pushing my hair back.',
            'I rub my hands together when I\'m exited, or when I have a plan.',
            'I snap my fingers to help me remember things.'
        ]
    ],
    [
        [
            'I am very good at keeping eye contact.'
        ],
        [
            'I struggle to maintain eye contact.',
            'I\'m always looking around. I\'m easily distracted.',
            'I find myself looking down a lot.',
            'Eye contact is not my priority. I only look at what I\'m doing.',
            'My eyes drift to the ceiling when I\'m thinking.'
        ]
    ],
    [
        [
            'My face is impossible to read.'
        ],
        [
            'I bite my lip when I\'m concentrating.',
            'I wrinkle my nose when I\'m frustrated.',
            'My face is very expressive.',
            'I frequently have one eyebrow raised.',
            'My eyes drift to the ceiling when I\'m thinking.'
        ]
    ],
    [
        [
            'I walk in long, slow strides.'
        ],
        [
            'I speed-walk everywhere I go.'
        ]
    ],
    [
        [
            `I am a brilliant speaker, captivating individuals and crowds.`
        ],
        [
            `I get really bad stage-fright.`,
            'I have a hard time finding my voice.',
            'I talk so fast that I often mix up words.',
            'I have trouble finishing a sentence. My voice trails off.',
            'My voice can be monotone at times.',
            'I mumble the words I really want to say, but everything else is loud and clear.',
            'My voice is soft, even when I want to speak up.'
        ]
    ],
    [
        [
            `I'm an athlete, and I'm best at swimming.`
        ],
        [
            `I stay away from water. I'm afraid of drowning.`
        ]
    ],
    [
        [
            `I'm an athlete, and I'm best at acrobatics.`
        ],
        [
            `I'm deathly afraid of heights.`
        ]
    ],
    [
        [
            'I have a hard time finding my voice, even when I need to speak.'
        ],
        [
            `I am very persuasive.`,
            `I'm a good liar. I can make anyone believe anything.`,
            'I speak very rapidly, but I articulate well.',
            'I talk so fast that I often mix up words.',
            'The pitch of my voice is a rollercoaster, always rising and falling.',
            'I have a dynamic voice. My volume, speed, and tone are always changing.',
            'I mumble the words I really want to say, but everything else is loud and clear.',
            'I have no volume control. When I open my mouth, the whole world hears.',
            'When I speak, I always sound excited.'
        ]
    ],
    [
        [
            'I\'m blind.'
        ],
        [
            'A great book is all I need to have a good time.',
            'I adore all cute animals.',
            'I\'m always up for a good movie.',
            'Fine art is a priceless treasure in my eyes.',
            `I have read hundreds, if not thousands, of books.`,
            `I'm great with computers.`,
            `I make great art. My best medium is acrylic paint.`,
            `I make great art. My best medium is oil paint.`,
            `I make great art. My best medium is watercolor paint.`,
            `I make great art. My best medium is pencil.`,
            `I make great art. My best medium is colored pencil.`,
            `I make great art. My best medium is crayon.`,
            `I make great art. My best medium is charcoal.`,
            `I make great art. My best medium is pastel.`,
            `I make great art. My best medium is oil pastel.`,
            `I make great art. My best medium is clay.`,
            `I make great art. My best medium is marker.`,
            `I am a blacksmith, and I do a fine job.`,
            `I am a glassblower, and I do a fine job.`,
            `I am a jeweler, and I do a fine job.`,
            `I'm an athlete, and I'm best at baseball.`,
            `I'm an athlete, and I'm best at basketball.`,
            `I'm an athlete, and I'm best at football.`,
            `I'm an athlete, and I'm best at soccer.`,
            `I'm an athlete, and I'm best at bowling.`,
            `I'm an athlete, and I'm best at boxing.`,
            `I'm an athlete, and I'm best at golf.`,
            `I'm an athlete, and I'm best at hockey.`,
            `I'm an athlete, and I'm best at tennis.`,
            `I'm an athlete, and I'm best at running.`,
            `I'm an athlete, and I'm best at fencing.`,
            `I'm an athlete, and I'm best at martial arts.`,
            `I'm an athlete, and I'm best at acrobatics.`,
            `I'm an athlete, and I'm best at swimming.`,
            `Keep the light on. I'm afraid of the dark.`,
            `I shy of camera lenses.`
        ]
    ],
    [
        [
            'I\'m deaf.'
        ],
        [
            'My favorite music always brightens my spirits.',
            `Music is my specialty. I play the piano.`,
            `Music is my specialty. I play the violin.`,
            `Music is my specialty. I play the viola.`,
            `Music is my specialty. I play the cello.`,
            `Music is my specialty. I play the upright bass.`,
            `Music is my specialty. I play the bass.`,
            `Music is my specialty. I play the guitar.`,
            `Music is my specialty. I play the drums.`,
            `Music is my specialty. I play the trumpet.`,
            `Music is my specialty. I play the french horn.`,
            `Music is my specialty. I play the clarinet.`,
            `Music is my specialty. I play the flute.`,
            `Music is my specialty. I play the tuba.`,
            `Music is my specialty. I play the euphonium.`,
            `Music is my specialty. I play the saxophone.`,
            `I am a talented singer.`,
            `I am a gifted writer. I mostly write musicals.`,
            `I am a brilliant speaker, captivating individuals and crowds.`
        ]
    ],
    [
        [
            'I\'m missing an arm.'
        ],
        [
            `I'm an athlete, and I'm best at baseball.`,
            `I'm an athlete, and I'm best at basketball.`,
            `I'm an athlete, and I'm best at football.`,
            `I'm an athlete, and I'm best at boxing.`,
            `I'm an athlete, and I'm best at golf.`,
            `I'm an athlete, and I'm best at hockey.`,
            `I'm an athlete, and I'm best at martial arts.`,
            `I'm an athlete, and I'm best at acrobatics.`,
            `I'm an athlete, and I'm best at swimming.`
        ]
    ]
];

// Define functions that select and/or return character attributes

function getGender() {
    let gender = document.getElementById('gender').textContent;
    return gender
};

function getHeight() {
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
    return [heightRaw, height];
};

function getWeight(heightRaw) {
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
    return weight + ' lb';
};

function getHairColor() {
    let hairColorElement = document.getElementById('hair_color');
    let hairColor = choice(hairColors);
    hairColorElement.textContent = hairColor;
    return hairColor;
};

function getEyeColor() {
    let eyeColorElement = document.getElementById('eye_color');
    let eyeColor = choice(eyeColors);
    eyeColorElement.textContent = eyeColor;
    return eyeColor;
};

function getUniqueAttribute() {
    let uniqueAttributeElement = document.getElementById('unique_attribute');
    let uniqueAttribute = choice(uniqueAttributes);
    uniqueAttributeElement.textContent = uniqueAttribute;
    return uniqueAttribute;
};

function getFavoriteClothes() {
    let favoriteClothes = favoriteClothesGeneric;
    if (getGender() === 'Male') {
        favoriteClothes = favoriteClothes.concat(favoriteClothesMale);
    }
    else {
        favoriteClothes = favoriteClothes.concat(favoriteClothesFemale);
    }
    let favoriteClothesElement = document.getElementById('favorite_clothes');
    let favoriteClothesChoice = choice(favoriteClothes);
    favoriteClothesElement.textContent = favoriteClothesChoice;
    return favoriteClothesChoice;
};

function getHairStyle() {
    let hairElement = document.getElementById('hair');
    let hair;
    if (getGender() === 'Male') {
        hair = choice(maleHair);
    }
    else {
        hair = choice(femaleHair);
    }
    hairElement.textContent = hair;
    return hair;
};

function getMannerisms() {
    let mannerismsOneElement = document.getElementById('mannerism_one');
    let mannerismsTwoElement = document.getElementById('mannerism_two');
    let mannerismOne = choice(mannerisms);
    let mannerismTwo = choice(mannerisms);
    while (mannerismOne === mannerismTwo) {
        mannerismTwo = choice(mannerisms);
    }
    mannerismsOneElement.textContent = mannerismOne;
    mannerismsTwoElement.textContent = mannerismTwo;
    return [mannerismOne, mannerismTwo];
};

function getSpeakingStyle() {
    let speakingStyleElement = document.getElementById('speaking_style');
    let speakingStyle = choice(speakingStyles);
    speakingStyleElement.textContent = speakingStyle;
    return speakingStyle;
};

function getSkill() {
    let skillElement = document.getElementById('skill');
    let skill = choice(skills);
    skillElement.textContent = skill;
    return skill;
};

function getFlaw() {
    let flawElement = document.getElementById('flaw');
    let flaw = choice(flaws);
    flawElement.textContent = flaw;
    return flaw;
};

function getFear() {
    let fearElement = document.getElementById('fear');
    let fear = choice(fears);
    fearElement.textContent = fear;
    return fear;
};

function getFavoriteThing() {
    let favoriteThingElement = document.getElementById('favorite');
    let favoriteThing = choice(favoriteThings);
    favoriteThingElement.textContent = favoriteThing;
    return favoriteThing
};

// Select character attributes

function select() {
    let heightAttributes = getHeight();
    let heightRaw = heightAttributes[0];
    let height = heightAttributes[1];
    let weight = getWeight(heightRaw);
    let hairColor = getHairColor();
    let eyeColor = getEyeColor();
    let uniqueAttribute = getUniqueAttribute();
    let favoriteClothesChoice = getFavoriteClothes();
    let hairStyle = getHairStyle();
    let mannerismsChoice = getMannerisms();
    let mannerismOne = mannerismsChoice[0];
    let mannerismTwo = mannerismsChoice[1];
    let speakingStyle = getSpeakingStyle();
    let skill = getSkill();
    let flaw = getFlaw();
    let fear = getFear();
    let favoriteThing = getFavoriteThing();

    // Ensure that no attributes are mutually exclusive

    let allAttributes = [
        mannerismOne,
        mannerismTwo,
        speakingStyle,
        skill,
        flaw,
        fear
    ];
    let effectiveScramble = false;
    while (!effectiveScramble) {
        effectiveScramble = true;
        for (let i = 0; i < exclusions.length; i++) {
            let firstMatch = false;
            let secondMatch = false;
            let firstAttribute;
            let secondAttribute;
            for (let j = 0; j < allAttributes.length; j++) {
                for (let k = 0; k < exclusions[i][0].length; k++) {
                    if (allAttributes[j] === exclusions[i][0][k]) {
                        firstMatch = true;
                        firstAttribute = allAttributes[j];
                    }
                }
                for (let k = 0; k < exclusions[i][1].length; k++) {
                    if (allAttributes[j] === exclusions[i][1][k]) {
                        secondMatch = true;
                        secondAttribute = allAttributes[j];
                    }
                }
            }
            if (firstMatch && secondMatch) {
                effectiveScramble = false;
                if (secondAttribute === mannerismOne) {
                    mannerismOne = choice(mannerisms);
                    let mannerismsOneElement = document.getElementById('mannerism_one');
                    mannerismsOneElement.textContent = mannerismOne;
                }
                else if (secondAttribute === mannerismTwo) {
                    mannerismTwo = choice(mannerisms);
                    let mannerismsTwoElement = document.getElementById('mannerism_two');
                    mannerismsTwoElement.textContent = mannerismTwo;
                }
                else if (secondAttribute === speakingStyle) {
                    speakingStyle = getSpeakingStyle();
                }
                else if (secondAttribute === skill) {
                    skill = getSkill();
                }
                else if (secondAttribute === flaw) {
                    flaw = getFlaw();
                }
                else if (secondAttribute === fear) {
                    fear = getFear();
                }
                else {
                    mannerismTwo = choice(mannerisms);
                    let mannerismsTwoElement = document.getElementById('mannerism_two');
                    mannerismsTwoElement.textContent = mannerismTwo;
                    speakingStyle = getSpeakingStyle();
                    skill = getSkill();
                    flaw = getFlaw();
                    fear = getFear();
                }
                allAttributes = [
                    mannerismOne,
                    mannerismTwo,
                    speakingStyle,
                    skill,
                    flaw,
                    fear
                ];
                break;
            }
        }
        if (effectiveScramble) {
            break;
        }
    }
};

// Scramble all attributes

function scramble() {
    defineClothes();
    defineUniqueAttributes();
    defineSkills();
    defineFlaws();
    defineFears();
    select();
};

// Initial scramble on page load

scramble();
