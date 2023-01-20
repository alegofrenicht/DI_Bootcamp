// Exercise 1: Simple If/Else Statement
// Instructions
// 1. Create 2 variables, x and y. Each of them should have a different numeric value.
// 2. Write an if/else statement that checks which number is bigger.
console.log('Exercise 1')

let x = 1;
let y = 2;

if (x > y){
    console.log(`${x} is the biggest number`)
}
else {
    console.log(`${y} is the biggest number`)
}


// Exercise 2: Chihuahua
// Instructions
// 1. Create a variable called newDog where it’s value is “Chihuahua”.
// 2. Check and display how many letters are in newDog.
// 3. Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
// 4. Check if the variable newDog is equal to “Chihuahua”
//  - if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
//  - else, console.log ‘I dont care, I prefer cats’
console.log('Exercise 2')

let newDog = "Chihuahua"
console.log(newDog.length)
console.log(newDog.toUpperCase())
console.log(newDog.toLowerCase())

if (newDog === 'Chihuahua'){
    console.log('I love Chihuahuas, it’s my favorite dog breed')
}
else {
    console.log('I dont care, I prefer cats')
}


// 🌟 Exercise 3: Even Or Odd
// Instructions
// 1. Prompt the user for a number and save it to a variable.
// 2. Check whether the variable is even or odd.
//  - If it is even, display: “x is an even number”. Where x is the actual number the user chose.
//  - If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.
console.log('Exercise 3')

let num = Number(prompt('Enter your number:'))
if (num % 2 === 0){
    alert(`${num} is an even number`)
    console.log(`${num} is an even number`)
}
else {
    alert(`${num} is an odd number`)
    console.log(`${num} is an odd number`)
}


// 🌟 Exercise 4: Group Chat
// Instructions
// Below is an array of users that are online in a group chat.
//
// const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

// 1. Using the array above, console.log the number of users that are connected to the group chat based on the following rules:
//  - If there is no users (the users array is empty), console.log “no one is online”.
//  - If there is 1 user, console.log “<name_user> is online”.
//  - If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
//  - If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.
//    For example, if there are 5 users, it should display:
//      name_user1, name_user2 and 3 more are online
console.log('Exercise 4')

const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let amount = users.length

switch (amount) {
    case 0:
        console.log(`no one is online`);
        break
    case 1:
        console.log(`${users} is online`);
        break;
    case 2:
        console.log(`${users[0]} and ${users[1]} are online`);
        break;
    default:
        console.log(`${users[0]}, ${users[1]} and ${amount - 2} more are online`);
}

