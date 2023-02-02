// Recreate the to-do list above:
//
// Create an HTML, CSS and a JS file.
//
// In the HTML file
// create a form with one input type="text", and a “Submit” button.
// add an empty div below the form
// <div class="listTasks"></div>
//
// In the js file, you must add the following functionalities:
// Create an empty array : const tasks = [];
//
// Create a function called addTask(). As soon as the user clicks on the button:
// check that the input is not empty,
// then add it to the array (ie. add the text of the task)
// then add it to the DOM, below the form (in the <div class="listTasks"></div>) .
// Each new task added should have (starting from left to right - check out the image at the top of the page)
// a “X” button. Use font awesome for the “X” button.
// an input type="checkbox". The label of the input is the task added by the user.

let div_tasks = document.getElementsByClassName('listTasks')[0]
let form = document.getElementById('task-form')
let clear_button = document.getElementById('clear')
clear_button.addEventListener('click', function () {
  div_tasks.innerHTML = ''
    count = 0
})
form.addEventListener('submit', addTask)
let count = 1
function addTask(e){
    e.preventDefault()
    const tasks = []
    let inp = document.getElementsByTagName('input')[0]
    if (inp.value.length === 0 ){
        return alert('empty request')
    }
    else {
        if (count === 5){
            return alert('list is full')
        }
        tasks.push(inp.value)
        let new_form = document.createElement('form')
        let new_input = document.createElement('input')
        let new_label = document.createElement('label')
        new_input.type = 'checkbox'
        new_input.id  = `input_${count}`
        let inp_id = new_input.id
        count ++
        new_label.setAttribute('for', `${inp_id}`)
        new_input.style.margin = '0'
        new_label.textContent = tasks[0]
        new_label.style.fontSize = '30px'
        new_input.style.border = 'none'
        new_form.append(new_input, new_label)
        new_form.style.borderBottomStyle = 'outset'
        new_form.style.margin = '10px 40px'
        new_form.style.padding = '10px'
        new_label.style.marginLeft = '20px'
        let flag = true
        new_input.addEventListener('click', function(){
            console.log(flag)
            if (flag){
                new_label.style.textDecoration = 'line-through'
                new_label.style.color = '#fd5c81'
                flag = false
            } else {
                new_label.style.textDecoration = 'none'
                new_label.style.color = 'black'
                flag = true
            }
            })
        div_tasks.append(new_form)
    }
}