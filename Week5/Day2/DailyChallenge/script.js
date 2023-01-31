// Instructions
// In todays exercise we will be creating a Mad Libs game.
// If you’ve never played this game, a mad lib is a game where you fill in a bunch of blank inputs with different word types (ie : noun, adjective, verb), and then a story is generated based on the words you chose, and sometimes the story is surprisingly funny.
//
// In this exercise you work with the HTML code presented below.
//
// Follow these steps :
//
// 1. Get the value of each of the inputs in the HTML file when the form is submitted. Remember the event.preventDefault()
// 2. Make sure the values are not empty
// 3. Write a story that uses each of the values.
// 4. Make sure you check the console for errors when playing the game.
// 5. Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user). The user could click the button at least three times and get a new story. Display the stories randomly.

let btn = document.getElementById('lib-button')
btn.setAttribute('type', 'submit')
let story = ['adj', 'noun', 'verb', 'name', 'place']
let allWords = []
let form = document.getElementById('libform')
form.addEventListener('submit', sub)
function sub(e){
    e.preventDefault()
    let inputs = document.getElementsByTagName('input')
    for (let input of inputs){
        let val = input.value
        if (val.length < 1){
            alert('blank line!')
        } else{
            allWords.push(val)
        }
    }
    for (let word in story){
        story[word] = allWords[word]
    }
    let span = document.getElementById('story')
    span.style.fontSize = '20px'
    span.textContent = story.join(' ')
}

