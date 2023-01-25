// 🌟 Exercise 1 : Information
console.log('Exercise 1')
// Instructions
// Part I : function with no parameters
//
// 1. Create a function called infoAboutMe() that takes no parameter.
// 2. The function should console.log a sentence about you (ie. your name, age, hobbies ect…).
// 3. Call the function.

function infoAboutMe(){
    console.log('My name is Alex, I\'m 28, fond of programming')
}
infoAboutMe()

// Part II : function with three parameters
//
// 1. Create a function called infoAboutPerson(personName, personAge, personFavoriteColor) that takes 3 parameters.
// 2. The function should console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
// 3. Call the function twice with the following arguments:
//      infoAboutPerson("David", 45, "blue")
//      infoAboutPerson("Josh", 12, "yellow")

function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log(`You name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`)
}

infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")


// 🌟 Exercise 2 : Tips
console.log('Exercise 2')
// Instructions
// John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.
//
// 1. Create a function named calculateTip() that takes no parameter.
//
// 2. Inside the function, use prompt to ask John for the amount of the bill.
//
// 3. Here are the rules
//    - If the bill is less than $50, tip 20%.
//    - If the bill is between $50 and $200, tip 15%.
//    - If the bill is more than $200, tip 10%.
//
// 4. Console.log the tip amount and the final bill (bill + tip).
//
// 5. Call the calculateTip() function.


function  calculateTip() {
    let bill = Number(prompt('How much is the bill?'))
    let tip = 0
    if (bill < 50) {
        tip = bill / 100 * 20
    }
    else if (50 < bill < 200) {
        tip = bill / 100 * 15
    }
    else if (bill > 200) {
        tip = bill / 100 * 10
    }
    console.log(`Final bill is ${bill + tip}\$`)
}

calculateTip()


// 🌟 Exercise 3 : Find The Numbers Divisible By 23
console.log('Exercise 3')
// Instructions
// 1. Create a function call isDivisible() that takes no parameter.
//
// 2. In the function, loop through numbers 0 to 500.
//
// 3. Console.log all the numbers divisible by 23.
//
// 4. At the end, console.log the sum of all numbers that are divisible by 23.
//
// Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 368
// 391 414 437 460 483
// Sum : 5313
//
//
// 5. Bonus: Add a parameter divisor to the function.
//
// isDivisible(divisor)
//
// Example:
// isDivisible(3) : Console.log all the numbers divisible by 3, and their sum
// isDivisible(45) : Console.log all the numbers divisible by 45, and their sum

function isDivisible(num){
    const numbers = []
    let sum = 0
    for (let i=0; i < 500; i++){
        if (i % num === 0){
            numbers.push(i)
            sum = sum + i
        }
    }
    console.log(`Outcome: ${numbers.join(' ')}`)
    console.log(`Sum: ${sum}`)
}

// isDivisible(prompt('Enter any number: '))


// 🌟 Exercise 4 : Shopping List
console.log('Exercise 4')
// Instructions
const stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

const prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}
// Add the stock and prices objects to your js file.
//
// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.
//
// Create a function called myBill() that takes no parameters.
//
// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.
//
// Call the myBill() function.
//
// Bonus: If the item is in stock, decrease the item’s stock by 1

const shoppingList = ['banana', 'orange', 'apple']

function myBill(){
    let total = 0
    for (item of shoppingList){
        console.log(item)
        if (item in stock && stock[item] !== 0){
            total = total + prices[item]
        }
    }
    return total
}

console.log(myBill())


// Exercise 5 : What’s In My Wallet ?
console.log('Exercise 5')
// Instructions
// Note: Read the illustration (point 4), while reading the instructions
//
// 1. Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
//      - an item price
//      - and an array representing the amount of change in your pocket.
//
// 2. In the function, determine whether or not you can afford the item.
//      - If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
//      - If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false
//
// 3. Change will always be represented in the following order: quarters, dimes, nickels, pennies.
//      A quarters is 0.25
//      A dimes is 0.10
//      A nickel is 0.05
//      A penny is 0.01
//
//
// 4. To illustrate:
//
// After you created the function, invoke it like this:
//
//     changeEnough(4.25, [25, 20, 5, 0])
// The value 4.25 represents the item’s price
// The array [25, 20, 5, 0] represents 25 quarters, 20 dimes, 5 nickels and 0 pennies.
// The function should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)
//
//
// Examples
//
// changeEnough(14.11, [2,100,0,0]) => returns false
// changeEnough(0.75, [0,0,20,5]) => returns true

function changeEnough(itemPrice, amountOfChange){
    let change = 0
    for (coin in amountOfChange){
        coin = Number(coin)
        if (coin === 0){
            change = change + (amountOfChange[coin] * 0.25)
        }
        else if (coin === 1){
            change = change + (amountOfChange[coin] * 0.10)
        }
        else if (coin === 2){
            change = change + (amountOfChange[coin] * 0.05)
        }
        else if (coin === 3){
            change = change + (amountOfChange[coin] * 0.01)
        }
    }
    if (itemPrice > change){
        return `You can\'t afford this`
    }
    else {
        return 'You can afford this'
    }
}

console.log(changeEnough(14.11, [2,100,0,0]))
console.log(changeEnough(0.75, [0,0,20,5]))


// 🌟 Exercise 6 : Vacations Costs
console.log('Exercise 6')
// Instructions
// Let’s create functions that calculate your vacation’s costs:
//
// 1.Define a function called hotelCost().
//      It should ask the user for the number of nights they would like to stay in the hotel.
//      If the user doesn’t answer or if the answer is not a number, ask again.
//      The hotel costs $140 per night. The function should return the total price of the hotel.
function hotelCost(){
    quest = Number(prompt('How long you would stay in our hotel? Choose the number of days'))
    while (quest < 1 || isNaN(quest) === true){
        quest = Number(prompt('How long you would stay in our hotel? Choose the number of days'))
    }

    return quest * 140
}

// 2. Define a function called planeRideCost().
//      It should ask the user for their destination.
//      If the user doesn’t answer or if the answer is not a string, ask again.
//      The function should return a different price depending on the location.
//          - “London”: 183$
//          - “Paris” : 220$
//          - All other destination : 300$
function planeRideCost(){
    let destntn = prompt('What\'s your destination?')
    let price = 0
    while (!isNaN(destntn)){
        destntn = prompt('What\'s your destination?')
    }
    if (destntn.toLowerCase() === 'london'){
        price = 183
    }
    else if (destntn.toLowerCase() === 'paris'){
        price = 220
    }
    else {
        price = 300
    }
    return price
}

// 3. Define a function called rentalCarCost().
//      It should ask the user for the number of days they would like to rent the car.
//      If the user doesn’t answer or if the answer is not a number, ask again.
//      Calculate the cost to rent the car. The car costs $40 everyday.
//          - If the user rents a car for more than 10 days, they get a 5% discount.
//      The function should return the total price of the car rental.

function rentalCarCost(){
    rental = Number(prompt('How long you would rent a car? Choose the number of days'))
    while (rental < 1 || isNaN(rental) === true){
        rental = Number(prompt('How long you would rent a car? Choose the number of days'))
    }
    let price = rental * 40
    if (rental > 10){
        return price - (price / 100 * 5)
    }
    return price
}
// 4. Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().
//

// 5. Call the function totalVacationCost()
//
function totalVacationCost(){
    return `The car cost: \$${rentalCarCost()}, the hotel cost: \$${hotelCost()}, the plane tickets cost: \$${planeRideCost()}`}
console.log(totalVacationCost())