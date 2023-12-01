
// Variable Declaration
let myDog = 'Bean'; // let defines a variable who's value can be changed
console.log(myDog);

myDog = "Bitch Boy";
console.log(myDog);

const myCat = "Mr. Meow"; // const defines a variable who's value cannot be changed
console.log(myCat);

// myCat = "lucky";
// console.log(myCat);

// Objects

let person = {
    name: 'Gurjot',
    age: 28,
};

console.log(person);
// Dot Notation
console.log(person.name);
person.name = "Gur"
console.log(person.name);

// Bracket Notation - good for runntime selections
let selection = 'name'
person[selection] = 'Gurjot'
console.log(person['name'])

// functions
function greet() {
    window.alert('Hello World');
}


// onload = function () {
//     window.alert('page loaded!');
// }

function showText() {

}

document.getElementById("myButton").onclick = function () {
    window.alert('Hello World');
}

// What if we want to say hello to the users name?
let username = '';

document.getElementById("submit-name").onclick = function () {
    username = document.getElementById("name").value;
    console.log(username);
    // window.alert('Hello ' + username + "!");
    document.getElementById("change-me").innerHTML = "Hello " + username + "!";
}

let isHidden = false;

document.getElementById("showhide").onclick = function () {
    if (isHidden) {
        document.getElementById("text-show-hide").style.display = "block";
    }
    else {
        document.getElementById("text-show-hide").style.display = "none";
    }
}

// arrow functions

const DoSomething = () => {
    console.log("Hello World");
}

function HideShow() {
    if (isHidden) {
        document.getElementById("text-show-hide").innerHTML.d
    }
}


// This structure is specific to react
// const MyComponent = () => {
//     return
//     <div>

//     </div>
// }






// .innerHTML writes into an html element
//To access an HTML element, JavaScript can use the document.getElementById(id) method.
//The id attribute defines the HTML element. The innerHTML property defines the HTML content:
