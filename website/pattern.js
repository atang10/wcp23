/*
grid variable and function toggleColor is to change a color for the table. This function is not needed anymore.
var canvas,ctx, and flag is used as the object that holds the canvas.
var first allows you to draw until you don't use your mouse.
y is how thick the pen you want to be.
*/
var grid = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
var canvas, ctx, flag = false,
prevX = 0,
currX = 0,
prevY = 0,
currY = 0,
dot_flag = false;
var first = 0;
var x = "black",
y = 2; //4
function toggleColor (index){
    var box = document.getElementsByTagName("td");
    color = box[index].style.backgroundColor;
    if(color.localeCompare("blue") == 0) {
        box[index].style.backgroundColor = "white";
        grid[index] = 0;
        }
    else {
        box[index].style.backgroundColor = "blue";
        grid[index] =1;
    }
}   
function init() {
    //initilize and add an event listener based off of the state of the mouse.
    canvas = document.getElementById('can');
    ctx = canvas.getContext("2d");
    w = canvas.width;
    h = canvas.height;

    canvas.addEventListener("mousemove", function (e) {
        findxy('move', e)
    }, false);
    canvas.addEventListener("mousedown", function (e) {
        findxy('down', e)
    }, false);
    canvas.addEventListener("mouseup", function (e) {
        findxy('up', e)
    }, false);
    canvas.addEventListener("mouseout", function (e) {
        findxy('out', e)
    }, false);
}
//Draws based to the position where your mouse is.
function draw() {
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
    ctx.lineTo(currX, currY);
    ctx.strokeStyle = x;
    ctx.lineWidth = y;
    ctx.stroke();
    ctx.closePath();
}
//Erases the whole canvas drawing.
function erase() {
    var m = confirm("Want to clear");
    first = 0; //resets first to 0 so you can redraw again.
    if (m) {
        ctx.clearRect(0, 0, w, h);
        document.getElementById("canvasimg").style.display = "none";
    }
}
function save() {
    document.getElementById("canvasimg").style.border = "2px solid";
    var dataURL = canvas.toDataURL();
    document.getElementById("canvasimg").src = dataURL;
    document.getElementById("canvasimg").style.display = "inline";
}
//Function that calculates the position
function findxy(res, e) {
    //Mouse is clicked in down state.
    if (res == 'down') {
        prevX = currX;
        prevY = currY;
        currX = e.clientX - canvas.offsetLeft;
        //currY = e.clientY - canvas.offsetTop;
        currY = e.clientY - canvas.getBoundingClientRect().top;
        //console.log("offsetLeft= " + canvas.getBoundingClientRect().left+"offsetTop= " + canvas.getBoundingClientRect().top + "mousex=" + e.clientX + "mousey=" + e.clientY+ "currX= "+currX +"currY"+ currY);
        //flag = true;
        //dot_flag = true;
         //console.log(first);
         if (first < 1){
            flag = true;
            dot_flag = true;
        }
        if (dot_flag) {
            ctx.beginPath();
            ctx.fillStyle = x;
            ctx.fillRect(currX, currY, 2, 2);
            ctx.closePath();
            first = first + 1;
            dot_flag = false;
        }
    }
    //If out of zone or picked up your pen.
    if (res == 'up' || res == "out") {
        flag = false;
    }
    //if starting to move your mouse.
    if (res == 'move') {
        if (flag) {
            prevX = currX;
            prevY = currY;
            currX = e.clientX - canvas.offsetLeft;
            //currY = e.clientY - canvas.offsetTop;
            currY = e.clientY - canvas.getBoundingClientRect().top;
            draw();
        }
    }
}
//Function originally to change color of your pen
function color_switch(obj) {
    switch (obj.id) {
        case "black":
            x = "black";
            break;
        case "white":
            x = "white";
            break;
    }
    if (x == "white") y = 14;
    else y = 2;
}