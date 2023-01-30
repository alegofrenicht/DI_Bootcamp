// Exercise 5 : Event Listeners
// 1. Add many events listeners to one element on your webpage. Use the click, mouseover, mouseout and dblclick events.
// 2. Each listener should do a different thing, for instance - change position x, change position y, change color, change the font size… and more.

let content = document.getElementById('wp')

content.addEventListener('click', clickfunc)

function clickfunc(e){
    e.preventDefault()
    content.style.fontSize = '100px'
}

content.addEventListener('mouseover', moverfunc)

function moverfunc(e){
    e.preventDefault()
    content.style.color = 'red'
}

content.addEventListener('mouseout', moout)
function moout(e){
    e.preventDefault()
    content.style.transform =  'rotateZ(-30deg)'
}

content.addEventListener('dblclick', dblfunc)

function dblfunc(e){
    e.preventDefault()
    let span = document.createElement('span')
    span.textContent = 'it\'s my web page if you forgot'
    content.appendChild(span)
    let new_span = content.lastElementChild
    new_span.style.fontSize = `${content.style.fontSize / 1.5}px`
    new_span.style.color = 'blue'
}