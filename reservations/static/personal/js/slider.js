var number = Math.floor(Math.random() * 5) + 1;

var timer1 = 0
var timer2 = 0

function schowaj() {
    $("#slider").fadeOut(500);
}
function ustawslajd(nrslajdu) {
clearTimeout(timer1);
clearTimeout(timer2);
number=nrslajdu-1;
schowaj();
setTimeout("zmienslajd()",500);
}
function zmienslajd() {
    number++;
    if (number > 5) number = 1;
    var plik = "<img src=static/personal/img/slajd" + number + ".png/>";
    document.getElementById("slider").innerHTML = plik;
    $("#slider").fadeIn(500);
    timer1 = setTimeout("schowaj()", 7500);
    timer2 = setTimeout("zmienslajd()", 8000);

}