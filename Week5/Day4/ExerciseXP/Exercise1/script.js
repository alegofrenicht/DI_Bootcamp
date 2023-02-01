// Using this HTML code:
//
// <!DOCTYPE html>
//     <html>
//     <head>
//         <style>
//         p {
//           background: yellow;
//           color: red;
//         }
//         </style>
//     </head>
//     <body>
//         <div id="container"></div>
//         <button id="clear">Clear Interval</button>
//     </body>
//     </html>
//
//
// Part I
// 1. In your Javascript file, using setTimeout, call a function after 2 seconds.
// 2. The function will alert “Hello World”.
function helloWorld(){
    alert('Hello World')
}
setTimeout(helloWorld, 2000)
//
// Part II
// 1. In your Javascript file, using setTimeout, call a function after 2 seconds.
// 2. The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
function addDiv(){
    let div = document.getElementById('container')
    let newP = document.createElement('p')
    newP.textContent = 'Hello World'
    if (div.children.length < 5){
    div.appendChild(newP)
    } else {
        stopInterval()
    }

}
// setTimeout(addDiv, 2000)

// Part III
// 1. In your Javascript file, using setInterval, call a function every 2 seconds.

// 2. The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// 3. The interval will be cleared (ie. clearInterval), when the user will click on the button.

let btn = document.getElementById('clear')
btn.addEventListener("click", stopInterval)
let funcInter = setInterval(addDiv, 2000)

function stopInterval(){
    clearInterval(funcInter)
}

// 4. Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.