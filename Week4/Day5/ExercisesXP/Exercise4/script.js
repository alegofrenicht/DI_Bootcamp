// Exercise 4 : My Book List
// Instructions
// Take a look at this link for help.
//
// The point of this challenge is to display a list of two books on your browser.
//
// 1. In the body of the HTML page, create an empty div:
// <div class="listBooks"></div>
// 2. In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
//      title,
//      author,
//      image : a url,
//      alreadyRead : which is a boolean (true or false).
const allBooks = [];

// 3. Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)
const book1 = {
    title: 'The Art of War',
    author: 'Sun Tzu',
    image : 'https://d1w7fb2mkkr3kw.cloudfront.net/assets/images/book/lrg/9781/7840/9781784048174.jpg',
    alreadyRead: true
}

const book2 = {
    title: 'Martin Eden',
    author: 'Jack London',
    image : 'https://static.insales-cdn.com/images/products/1/1343/341910847/0000000608697-1.jpg',
    alreadyRead: false
}
allBooks.push(book1, book2)
// 4. Requirements : All the instructions below need to be coded in the js file:
//  1. Using the DOM, render the books inside an HTML table (the HTML table must be added to the <div> created in part 1).
//     For each book :
//        You have to display the book’s title and the book’s author.
//        Example: HarryPotter written by JKRolling.
//        The width of the image has to be set to 100px.
//        If the book is already read. Set the color of the book’s details to red.
let table = document.createElement('table')
let thead_elem = document.createElement('thead')
table.append(thead_elem)
let tr_1 = document.createElement('tr')
thead_elem.append(tr_1)
let th_1 = document.createElement('th')
th_1.setAttribute('colspan', '2')
th_1.textContent = 'My Books\' list'
tr_1.append(th_1)
let tb_1 = document.createElement('tbody')
table.append(tb_1)
let tr_2 = document.createElement('tr')
if (book1.alreadyRead === true){
    tr_2.style.color = 'red'
}
tb_1.append(tr_2)
let td_1 = document.createElement('td')
td_1.textContent = `${book1.title} written by ${book1.author}`
let td_2 = document.createElement('td')
let img_1 = document.createElement('img')
img_1.setAttribute('src', `${book1.image}`)
img_1.setAttribute('width', '100px')
img_1.setAttribute('height', '100px')
td_2.append(img_1)
tr_2.append(td_1, td_2)
let tr_2_1 = document.createElement('tr')
if (book2.alreadyRead === true){
    tr_2_1.style.color = 'red'
}
tb_1.append(tr_2_1)
let td_1_1 = document.createElement('td')
td_1_1.textContent = `${book2.title} written by ${book2.author}`
let td_2_2 = document.createElement('td')
let img_2 = document.createElement('img')
img_2.setAttribute('src', `${book2.image}`)
img_2.setAttribute('width', '100px')
img_2.setAttribute('height', '100px')
td_2_2.append(img_2)
tr_2_1.append(td_1_1, td_2_2)
document.getElementsByTagName('div')[0].append(table)
console.log(document.body)


