// 1. Using a DOM property, retrieve the h1 and console.log it.
console.log(document.getElementsByTagName('h1')[0])

// 2. Using DOM methods, remove the last paragraph in the <article> tag.
document.getElementsByTagName('article')[0].lastElementChild.remove()

// 3. Add an event listener which will change the background color of the h2 to red, when it’s clicked on.
let h_two = document.getElementsByTagName('h2')[0]
h_two.onclick = function (){
    h_two.style.backgroundColor = 'red'
}
// 4. Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
let h_three = document.getElementsByTagName('h3')[0]
h_three.onclick = function (){
    h_three.style.display = 'none'
}

// 5. Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
document.getElementsByTagName('article')[0].append(document.createElement('button'))
let btn = document.getElementsByTagName('button')[0]
btn.textContent = 'press'
btn.onclick = function (){
    document.body.style.fontWeight = 'bold'
}
// 6. BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)
let h_one = document.getElementsByTagName('h1')[0]
h_one.onmouseover = function (){
    h_one.style.fontSize = `${Math.floor(Math.random() * 100)}px`
}
// 7. BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
let p_two = document.getElementsByTagName('p')[1]
p_two.onmouseover = function (){
    p_two.style.opacity = '0.5'
}