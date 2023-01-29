// 🌟 Exercise 2 : Users And Style
// Instructions
// <div>Users:</div>
// <ul>
//     <li>John</li>
//     <li>Pete</li>
// </ul>
//
//
//  1. Add the code above, to your HTML file
//
//  2. Add a “light blue” background color and some padding to the <div>.
document.querySelector('div').setAttribute('style', 'background-color: lightblue; padding: 20px')

//  3.Do not display the <li> that contains the text node “John”.
document.getElementsByTagName('li')[0].setAttribute('style', 'display: none')

//  4.Add a border to the <li> that contains the text node “Pete”.
document.getElementsByTagName('li')[1].setAttribute('style', 'border: 2px solid yellow')

//  5. Change the font size of the whole body.
document.body.setAttribute('style', 'size: 50vh')
//  6. Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).
