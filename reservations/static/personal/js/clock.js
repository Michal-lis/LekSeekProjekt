function odliczanie() {
    var dzisiaj = new Date();
    var dzien = dzisiaj.getDate();
    var miesiac = dzisiaj.getMonth() + 1;
    var rok = dzisiaj.getFullYear();
    var godzina = dzisiaj.getHours();
    if (godzina < 10) {
        godzina = "0" + godzina
    }
    var minuta = dzisiaj.getMinutes();
    if (minuta < 10) {
        minuta = "0" + minuta
    }
    var sekunda = dzisiaj.getSeconds();// w Javascript zaleca się ale nie jest obowiażkowe stosowanie średnika na koncu
    if (sekunda < 10) {
        sekunda = "0" + sekunda
    }
    document.getElementById("clock").innerHTML = dzien + "/" + miesiac + "/" + rok + "   " + godzina + ":" + minuta + ":" + sekunda;//to jest uchwyt JavaScripta
    setTimeout('odliczanie()', 1000);//wywoływanie innej funkcji po danym okresie
}
