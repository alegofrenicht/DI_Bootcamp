// Instructions
// Add this sentence to your HTML file then follow the steps :
//
// <p><strong>Hello</strong> I hope you are enjoying <strong>this</strong> class. At the
// <strong>end</strong> you <strong>will</strong> be great Developers!
// <strong>Enjoy</strong> the <strong>JavaScript </strong> lessons</p>
//
//
// In the JS file:
//
// 1. Declare a global variable named allBoldItems.
let allBoldItems = []

// 2. Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.

function getBold_items(){
    let bolds = document.getElementsByTagName('strong')
    for (let bold of bolds){
        allBoldItems.push(bold)
    }
}

// 3. Create a function called highlight() that changes the color of all the bold text to blue.
function highlight(){
    getBold_items()
    for (let bold of allBoldItems){
        bold.style.color = 'blue'
    }
}

// 4. Create a function called return_normal() that changes the color of all the bold text back to black.
function return_normal(){
    for (let bold of allBoldItems){
        bold.style.color = 'black'
    }
}
// 5. Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() on mouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example
let paragraph = document.getElementsByTagName('p')[0]
paragraph.addEventListener('mouseover', highlight)
paragraph.addEventListener('mouseout', return_normal)