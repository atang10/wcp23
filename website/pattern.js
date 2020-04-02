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
function draw() {
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
    ctx.lineTo(currX, currY);
    ctx.strokeStyle = x;
    ctx.lineWidth = y;
    ctx.stroke();
    ctx.closePath();
}
function erase() {
    var m = confirm("Want to clear");
    first = 0;
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
function findxy(res, e) {
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
    if (res == 'up' || res == "out") {
        flag = false;
    }
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