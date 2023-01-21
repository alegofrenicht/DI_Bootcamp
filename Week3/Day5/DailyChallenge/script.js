// Instructions
// 1. Write a JavaScript program that recreates the pattern below.
// 2. Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// 3. Do this Daily Challenge by youself, without looking at the answers on the internet.
let stars = '******'
for (index in stars){
    console.log(stars.slice(0, Number(index) + 1))
}