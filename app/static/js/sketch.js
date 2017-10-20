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

    predict = createButton('predict');
    predict.parent('prediction-button').addClass('btn-lg').addClass('btn-primary');
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
    const img = get();
    const base64 = img.canvas.toDataURL().replace('data:image/png;base64,', '');;
    const data = {
        img: base64
    }

    httpPost('/api/predict', data, success, error);

    function success(reply) {
        const result = JSON.parse(reply);
        console.log(result)
        $('#output').text(result.predicted_class);
        reset = true;
    }

    function error(reply) {
        console.log(reply)
    }
}