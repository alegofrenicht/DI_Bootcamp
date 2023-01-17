// Exercise 1: Your Favorite Food
// Instructions
// Store your favorite food into a variable.
//
// Store your favorite meal of the day into a variable (ie. breakfast, lunch or dinner)
//
// Console.log I eat <favorite food> at every <favorite meal>
console.log('Exercise 1 !!!!!!!!!!!!!!!!!!!!1')
let favourite_food = "spaghetti"
let favourite_meal = "breakfast"
console.log('I eat', favourite_food, 'at every', favourite_meal)
console.log('I eat ${favourite_food} at every ${favourite_meal}')

//  Exercise 2 : Series
// Instructions
// Part I
// Using this array : const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
//
// Create a variable named myWatchedSeriesLength that is equal to the number of series in the myWatchedSeries array.
//
// Create a variable named myWatchedSeriesSentence, that is equal to a sentence describing the series you watched
// For example : black mirror, money heist, and the big bang theory
//
// Console.log a sentence using both of the variables created above
// For example : I watched 3 series : black mirror, money heist, and the big bang theory
console.log('Exercise 2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"]
let myWatchedSeriesLength = myWatchedSeries.length
let myWatchedSeriesSentence = myWatchedSeries[0] + ', ' + myWatchedSeries[1] + ', and ' + myWatchedSeries[2]
let result = 'I watched ' + myWatchedSeriesLength + ' series : ' + myWatchedSeriesSentence
console.log(result)

// Part II
// Change the series “the big bang theory” to “friends”. Hint : You will need to use the index of “the big bang theory” series.
// Add, at the end of the array, the name of another series you watched.
// Add, at the beginning of the array, the name of your favorite series.
// Delete the series “black mirror”.
// Console.log the third letter of the series “money heist”.
// Finally, console.log the myWatchedSeries array, to see all the modifications you’ve made.

myWatchedSeries[2] = 'friends'
myWatchedSeries.push('peaky blinders')
myWatchedSeries.unshift('true detective')
myWatchedSeries.splice(1,1)
console.log(myWatchedSeries[1][2])
console.log(myWatchedSeries)

// Exercise 3 : The Temperature Converter
// Instructions
// Store a celsius temperature into a variable.
//
// Convert it to fahrenheit and console.log <temperature>°C is <temperature>°F.
// Hint : Should you create another variable to hold the temperature in fahrenheit? (ie. point 2)
// Hint: To convert a temperature from celsius to fahrenheit : Divide it by 5, then multiply it by 9, then add 32
console.log('Exercise 3 !!!!!!!!!!!!!!!!!!!!!!!!!')
let celsius_temp = 15
let farenheit_temp = celsius_temp / 5 * 9 + 32
console.log(celsius_temp.toString(), '\u00B0C is', farenheit_temp.toString(), '\u00B0F')

// Exercise 4 : Guess The Answers #1
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.
console.log('Exercise 4 !!!!!!!!!!!!!!!!!!!!!!!!')
let c;
let a = 34;
let b = 21;

// c variable isn't defined, so it is not going to be shown
console.log(a+b) //first expression
// Prediction: 55
// Actual: 55

a = 2;

console.log(a+b) //second expression
// Prediction: 23
// Actual: 23

// 4. Analyse the code below, what will be the outcome?

console.log( 3 + 4 + '5')
// Income: 75, because 3 + 4 are numbers and income of this operation will be 7, at the same time '5' is string, so we concatenate 7 and 5 and get string element which is '75'

// Exercise 5 : Guess The Answers #2
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.

// 1. What is the output of each of the expressions below?
console.log('Exercise 5 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

console.log(typeof(15))
// Prediction: number
// Actual: number

console.log(typeof 5.5)
// Prediction: number
// Actual: number

console.log(typeof NaN)
// Prediction:
// Actual:

console.log(typeof("hello"))
// Prediction:
// Actual:

console.log(typeof true)
// Prediction:
// Actual:

console.log(typeof(1 != 2))
// Prediction:
// Actual:

console.log("hamburger" + "s")
// Prediction: hamburgers
// Actual:

console.log("hamburgers" - "s")
// Prediction: hamburger
// Actual: NaN

console.log("1" + "3")
// Prediction: 13 because them both string and '+' is for concatenation
// Actual:

console.log("1" - "3")
// Prediction: -2 because '-' is numerical method
// Actual: -2

console.log("johnny" + 5)
// Prediction: johnny5
// Actual: johnny5

console.log("johnny" - 5)
// Prediction: NaN because '-' is numerical method and 'johnny' is not number
// Actual: NaN

console.log(99 * "hello")
// Prediction: hello 99 times
// Actual: NaN

console.log(1 != 1)
// Prediction: false
// Actual: false

console.log(1 == "1")
// Prediction: true because them equal
// Actual: true

console.log(1 === "1")
// Prediction: false because them are different types
// Actual: false


// Exercise 6 : Guess The Answers #3
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.
//
//
//
//1. What is the output of each of the expressions below?
console.log('Exercise 6 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

console.log(5 + "34")
// Prediction: 534
// Actual: 534

console.log(5 - "4")
// Prediction: 1
// Actual: 1

console.log(10 % 5)
// Prediction: 0 because after division nothing left and the result is integer
// Actual: 0

console.log(5 % 10)
// Prediction: 5 because 5 is less than 10 and can't be divided with integer result
// Actual: 5

console.log("Java" + "Script")
// Prediction: JavaScript
// Actual: JavaScript

console.log(" " + " ")
// Prediction: nothing
// Actual: nothing

console.log(" " + 0)
// Prediction: 0
// Actual: 0

console.log(true + true)
// Prediction: 2 because true is 1 as integer and false is 0
// Actual: 2

console.log(true + false)
// Prediction: 1
// Actual: 1

console.log(false + true)
// Prediction: 1
// Actual: 1

console.log(false - true)
// Prediction: -1
// Actual: -1

console.log(!true)
// Prediction: false because '!' means 'not' so it makes opposite of expression
// Actual: false

console.log(3 - 4)
// Prediction: -1
// Actual: -1

console.log("Bob" - "bill")
// Prediction: NaN because we can't subtract not numerical elements
// Actual: NaN
