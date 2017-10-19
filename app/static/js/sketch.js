let reset = false;
let drawing = false;

let canvas;
let predict;
let outputResult;

function setup() {
    canvas = createCanvas(400, 400);
    canvas.parent('draw-canvas');
    canvas.mousePressed(startDrawing);
    canvas.mouseReleased(stopDrawing);

    predict = createButton('predict')
    predict.mousePressed(onPredict);

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

function onPredict() {
    reset = true;
    print('predict');
}