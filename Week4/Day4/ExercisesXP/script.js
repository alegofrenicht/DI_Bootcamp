let num_bottles = Number(prompt('How many bottles do you want?'))
let take_down = 1
let it_them = 'it'
let bottle_s = 'bottles'
while (num_bottles > Number(0)){
    if (num_bottles < 2){
        bottle_s = 'bottle'
    }
    if (take_down > 1){
        it_them = 'them'
    }
    console.log(`${num_bottles} ${bottle_s} of beer on the wall
${num_bottles} ${bottle_s} of beer
Take ${take_down}, pass ${it_them} around`)
    if (Number(take_down) > Number(num_bottles)){
        break}
    num_bottles = num_bottles - Number(take_down)
    take_down ++
    console.log(`${num_bottles} ${bottle_s} of beer on the wall`)

}
console.log('no bottle of beer on the wall')