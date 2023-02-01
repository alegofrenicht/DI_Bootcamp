let color = null;
let mousedown = false;
let main = document.getElementById('main')
for (let i=0; i < 350; i++){
    let newDiv = document.createElement('div')
    main.appendChild(newDiv)
}
let body = document.getElementsByTagName("body")[0];
let color_blocks = document.querySelectorAll("#sidebar > *");
let fill_blocks = document.querySelectorAll("#main > *");
let clear_button = document.getElementsByTagName("button")[0];

clear_button.addEventListener('mousedown', function(){
    clear_button.style.transform = 'translateX(-3px)'
})

clear_button.addEventListener('mouseup', function(){
    clear_button.style.transform = 'translateX(3px)'
})
clear_button.addEventListener("click", function(){
    for (let fill_block of fill_blocks){
        fill_block.style.backgroundColor = "white";
    }
})

body.addEventListener("mousedown", function(){
    mousedown = true;
})

body.addEventListener("mouseup", function(){
    mousedown = false;
})


for (let color_block of color_blocks){
    color_block.addEventListener("click", function(e){
        color = e.target.style.backgroundColor;
    });
}

for (let fill_block of fill_blocks){
    fill_block.addEventListener("mousedown", function(e){
        if (color != null){
            e.target.style.backgroundColor = color;}
    });
    fill_block.addEventListener("mouseover", function(e){
        if (mousedown && color != null) {
            e.target.style.backgroundColor = color;
        }
    });
}
