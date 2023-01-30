// 🌟 Exercise 2 : Work With Forms
// 1. Retrieve the form and console.log it.
let forms = document.getElementsByTagName('form')[0]
console.log(forms)
// 2. Retrieve the inputs by their id and console.log them.
let fname = document.getElementById('fname')
let lname = document.getElementById('lname')
let submit = document.getElementById('submit')
console.log(fname, lname, submit)
// 3. Retrieve the inputs by their name attribute and console.log them.
console.log(document.getElementsByName('fname')[0])
console.log(document.getElementsByName('lname')[0])
// 4. When the user submits the form (ie. submit event listener)
//      use event.preventDefault(), why ?
//      get the values of the input tags,
//      make sure that they are not empty,
//      create an <li> per input value,
//      then append them to the <ul class="usersAnswer"></ul>, below the form.
// The output should be :
//
//      <ul class="usersAnswer">
//          <li>first name of the user</li>
//          <li>last name of the user</li>
//      </ul>

function submitfunc(e){
    e.preventDefault()
    let li_one = fname.value
    let li_two = lname.value
    if (li_one < 1 || li_two < 1){
        alert('don\'t leave blank form')
    }
    else {
        let lione = document.createElement('li')
        lione.textContent = li_one
        let litwo = document.createElement('li')
        litwo.textContent = li_two
        document.querySelector('.usersAnswer').append(lione, litwo)
    }

}
forms.addEventListener('submit', submitfunc, true)