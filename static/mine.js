function loadJson(selector) {
  return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
}

window.onload = function () {
  let jsonData = loadJson('#jsonData');  //Принятие запроса из базы Django

let text = jsonData.map((item) => item.question_text);
let array = jsonData.map((item) => item.question_number);
let array2 = [];
let arrayinp = [];
let color =[];
//let a = prompt();
let b = 1;
for(let i = 0; i < array.length; i++) {
    color.push("#fde23e");
    arrayinp.push(b);
    b = b + 1;
    array2.push(0);
}
console.log(array);
console.log(arrayinp);
for (let i = 0; i < 100; i++) {

    let rand_number = Math.floor(Math.random() * array.length);
    let temp = array[rand_number];

    let rand = Math.floor(Math.random() * array.length);
    array[rand_number] = array[rand];
    array[rand] = temp;
} //Создание массива случайных вопросов

let offset = 0;
let sector = 360 / array.length;

let myCanvas = document.getElementById("myCanvas"); //Отрисовка круга
myCanvas.width = 500;
myCanvas.height = 500;
let ctx = myCanvas.getContext("2d");

function drawSegment(ctx,centerX, centerY, radius, startAngle, endAngle, color ){
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.moveTo(centerX,centerY);
    ctx.arc(centerX, centerY, radius, startAngle, endAngle);
    ctx.closePath();
    ctx.fill();
}

let Piechart = function(options){
    this.options = options;
    this.canvas = options.canvas;
    this.ctx = this.canvas.getContext("2d");
    this.colors = options.colors;

    this.draw = function(){
        let color_index = 0;
        let start_angle = Math.PI * 3.5;
        for (let i = 0; i < this.options.data.length; i++) {
            let val = this.options.data[i];
            let slice_angle = 2 * Math.PI / arrayinp.length;

            drawSegment(
                this.ctx,
                this.canvas.width / 2,
                this.canvas.height / 2,
                Math.min(this.canvas.width / 2, this.canvas.height / 2),
                start_angle,
                start_angle + slice_angle,
                this.colors[color_index % this.colors.length]
            );
            let pieRadius = Math.min(this.canvas.width/1.2,this.canvas.height/1.2); //Отображение номера вопроса на "куске пирога"
            let labelX = this.canvas.width/2 + (pieRadius / 2) * Math.cos(start_angle + slice_angle/2);
            let labelY = this.canvas.height/2 + (pieRadius / 2) * Math.sin(start_angle + slice_angle/2);
            let labelText = val;
            this.ctx.fillStyle = "white";
            this.ctx.font = "bold 20px Arial";
            this.ctx.fillText(labelText+"", labelX,labelY);
            start_angle += slice_angle;
            color_index++;
            ctx.stroke();
        }
    }
}
let myPiechart = new Piechart(
    {
        canvas:myCanvas,
        data:arrayinp,
        colors:color
    }
);
myPiechart.draw();

for (let i = 0; i < array.length; i++) { //Логика анимации стрелки
    let r = 360 * (Math.floor(Math.random() * 3) + 1);
    let q = 0;
    if (i != 0) {
        q = array[i - 1];
    }
    if (q < array[i]) {
        array2[i] = offset + (array[i] - q) * sector + r;
    }else {
        array2[i] = offset + (360 - (q - array[i]) * sector) + r;
    }
    if (i == 0) {
        array2[i] =  array2[i] - sector / 2;
    }
    offset =  array2[i];
}
console.log(array);
console.log(array2);
let ptr = document.querySelector(".wheel_hand");
let o = 0;
ptr.addEventListener("click", function(){ //Запуск анимации стрелки
    ptr.style.transition = "transform "+2500 +"ms";
    ptr.style.transform = "rotate("+ (array2[o]) + "deg)";
    function update(){
        color[[array[o]] - 1] = "#937e88";
        myPiechart.draw();
        document.getElementById("p1").innerHTML=[text[array[o] - 1]];
        console.log(text);
        o = o + 1;
    }
    setTimeout(update, 2500);
    console.log(color);
})}
//window.onload = drawPie;
//ptr.style.transform = "rotate("+45 + "deg)"; #937e88
//ptr.style.transition = "transform "+1000 +"ms";