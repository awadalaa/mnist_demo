let reset = false;
let drawing = false;

let outputResult;
let submitButton;

function setup() {
    var canvas = createCanvas(400, 400);
    canvas.mousePressed(startDrawing);
    canvas.mouseReleased(stopDrawing);
    background(0);
}

function draw() {
    if (drawing) {
        stroke(255);
        strokeWeight(16);
        line(mouseX, mouseY, pmouseX, pmouseY);
    }
}

function startDrawing() {
    drawing = true;
    if (reset) {
        background(0);
        reset = false;
    }
}

function stopDrawing() {
    drawing = false;
}