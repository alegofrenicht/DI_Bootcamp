// 🌟 Exercise 1 : List Of People
console.log('Exercise 1')
// Part I - Review About Arrays
const people = ["Greg", "Mary", "Devon", "James"];
// 1. Write code to remove “Greg” from the people array.
people.shift()
// 2. Write code to replace “James” to “Jason”.
people[people.indexOf('James')] = 'Jason'
// 3. Write code to add your name to the end of the people array.
people[people.length] = 'Alex'
// 4. Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

console.log(people.indexOf('Mary'))
// 5. Write code to make a copy of the people array using the slice method.
//      - The copy should NOT include “Mary” or your name.
//      Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
//      Hint: Check out the documentation for the slice method
let newPeople = people.slice(1, people.length - 1)
// 6. Write code that gives the index of “Foo”. Why does it return -1 ?
console.log('!!!!')

console.log(people.indexOf('Foo'))
//It returns -1 because 'Foo element doesn't exists and is not the part of this array'
// 7. Create a variable called last which value is the last element of the array.
//    Hint: What is the relationship between the index of the last element in the array and the length of the array?
let last = String(people[people.length - 1])
// Part II - Loops
console.log('!!!!')
// 1. Using a loop, iterate through the people array and console.log each person.
for (name of people){
    console.log(name)
}
// 2. Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .
console.log('!!!!')
// Hint: take a look at the break statement in the lesson.

for (name of people){
    if (name === 'Jason'){
        break
    }
    else {
        console.log(name)
    }
}

// 🌟 Exercise 2 : Your Favorite Colors
console.log('Exercise 2')
// Instructions
// 1. Create an array called colors where the value is a list of your five favorite colors.

const colors = ['red', 'blue', 'black', 'yellow', 'white']
// 2. Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .

for (color in colors) {
    console.log(`My #${Number(color) + 1} choice is ${colors[color]}`)
}

// 3. Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
//    Hint : create an array of suffixes to do the Bonus
console.log('!!!!')

const suffixes = ['st', 'nd', 'rd', 'th', 'th']

for (color in colors) {
    console.log(`My ${Number(color) + 1}${suffixes[color]} choice is ${colors[color]}`)
}

// 🌟 Exercise 3 : Repeat The Question
console.log('Exercise 3')
// Instructions
// 1. Prompt the user for a number.
//    Hint : Check the data type you receive from the prompt (ie. Use the typeof method)
// let num_prompt = Number(prompt('Enter a number: '))
// console.log(num_prompt)
// 2. While the number is smaller than 10 continue asking the user for a new number.
//    Tip : Which while loop is more relevant for this situation?

// let num = 0
// while (num < 10){
//     num = Number(prompt('Enter a number: '))
// }

// 🌟 Exercise 4 : Building Management
console.log('Exercise 4')

// Review About Objects
// 1. Copy and paste the above object to your Javascript file.
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
// 2. Console.log the number of floors in the building.
console.log(building["numberOfFloors"])
// 3. Console.log how many apartments are on the floors 1 and 3.
console.log('!!!!')

console.log(`${building["numberOfAptByFloor"]["firstFloor"]} apartments on the floor 1 and ${building["numberOfAptByFloor"]["thirdFloor"]} - on the third`)
// 4. Console.log the name of the second tenant and the number of rooms he has in his apartment.
console.log('!!!!')

console.log(`${building["nameOfTenants"][1]} has ${building["numberOfRoomsAndRent"]["dan"][0]} rooms`)
// 5. Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.
let sarahs_rent = building["numberOfRoomsAndRent"]["sarah"][1]
let davids_rent = building["numberOfRoomsAndRent"]["david"][1]
let dans_rent = building["numberOfRoomsAndRent"]["dan"][1]
if (sarahs_rent + davids_rent > dans_rent ){
    building["numberOfRoomsAndRent"]["dan"][1] = 1200
}

//
// 🌟 Exercise 5 : Family
console.log('Exercise 5')
// Instructions
// 1. Create an object called family with a few key value pairs.
const family = {
    father: 'John',
    mother: 'Anne',
}
// 2. Using a for in loop, console.log the keys of the object.
for (member in family) {
    console.log(member)
}
// 3. Using a for in loop, console.log the values of the object.
console.log('!!!!')

for (member in family) {
    console.log(family[member])
}


// Exercise 6 : Rudolf
console.log('Exercise 6')
// Instructions
const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}
// 1. Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”
let sentence = ''
for (detail in details){
    sentence = sentence + detail + ' ' + details[detail] + ' '
}

console.log(sentence.slice(0, sentence.length - 1))


// Exercise 7 : Secret Group
console.log('Exercise 7')
// Instructions
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// 1. A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
//    Hint: a string is an array of letters
society = ''
for (name of names.sort()){
    society = society + name[0]
}
// 2. Console.log the name of their secret society. The output should be “ABJKPS”
console.log(society)







