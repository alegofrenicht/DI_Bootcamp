// Instructions
// <div id="container">Users:</div>
// <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
// </ul>
// <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
// </ul>
//
//
// 1. Add the code above, to your HTML file
//
// 2. Using Javascript:
//      1. Retrieve the div and console.log it
let div_one = document.getElementById('container')
console.log(div_one)
//      2. Change the name “Pete” to “Richard”.
document.getElementsByTagName('li')[1].innerHTML = 'Richard'
//      3. Change each first name of the two <ul>'s to your name.
for (let i=0; i < 2; i++){
    document.querySelectorAll('.list')[i].firstElementChild.textContent = 'Alex'
}
//      4. Delete the <li> that contains the text node “Sarah”.
// let lists_length = document.getElementsByTagName('li').length
// for (let i=0; i < lists_length ; i++){
//     let lists = document.getElementsByTagName('li')[i]
//     if (lists.textContent === 'Sarah'){
//         lists.remove()
//     }
// }

// 3. Bonus - Using Javascript:
//      1. Add a class called student_list to both of the <ul>'s.
//      2. Add the classes university and attendance to the first <ul>.
let uls = document.getElementsByTagName('ul')

for (let i=0; i < uls.length ; i++){
    uls[i].classList.add('student_list')
}

uls[0].classList.add('university', 'attendance')
