var number = Math.floor(Math.random() * 5) + 1;

function schowaj() {
    $("#slider").fadeOut(500);
}

function zmienslajd() {
    number++;
    if (number > 5) number = 1;
    var plik = "<img src=static/slajdy/slajd" + number + ".png/>";
    document.getElementById("slider").innerHTML = plik;
    $("#slider").fadeIn(500);
    setTimeout("schowaj()",7500);
    setTimeout("zmienslajd()", 8000);

}