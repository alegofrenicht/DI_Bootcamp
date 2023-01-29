// In this exercise we will be creating a webpage with a black background as the universe and we will fill the universe with planets and their moons.
// We will provide the HTML page.
// You only have to work with a JS file.
//
// 1. Create an array which value is the planets of the solar system.
const planets = [
    {name: 'Mercury', moons: 1},
    {name: 'Venus', moons: 0},
    {name: 'Earth', moons: 1},
    {name: 'Mars', moons: 2},
    {name: 'Jupiter', moons: 2},
    {name: 'Saturn', moons: 0},
    {name: 'Uranus', moons: 1},
    {name: 'Neptune', moons: 3}
]
const colors = ['#b6bac5', '#bf8639', '#06c', '#aa4200', '#e0ae6f', '#dfd3a9', '#82b3d1', '#77c2ec']
// 2. For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
// 3. Each planet should have a different background color. (Hint: you could add a new class to each planet - each class containing a different background-color).
// 4. Finally append each div to the <section> in the HTML (presented below).
for (let planet in planets){
    let newDiv = document.createElement("div")
    newDiv.className = `planet`
    newDiv.classList.add(planets[planet].name)
    newDiv.style.backgroundColor = colors[planet]
    document.getElementsByTagName('section')[0].append(newDiv)
      for (let moon = 0; moon < planets[planet].moons; moon++){
          let moondiv = document.createElement("div")
          moondiv.className = `moon`
          moondiv.style.left = `${moon * 50}px`
          document.getElementsByClassName(`planet ${planets[planet].name}`)[0].appendChild(moondiv)
    }
}
// 5. Bonus: Do the same process to create the moons.
// Be careful, each planet has a certain amount of moons. How should you display them?
// Should you still use an array for the planets ? Or an array of objects ?