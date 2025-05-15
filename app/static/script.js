// script.js

const semaforo = document.getElementById("punto-semaforo");

function atualizarPonto() {
    fetch("/api/punto_rojo")
        .then(response => response.json())
        .then(data => {
            semaforo.style.left = data.left;
            semaforo.style.top = data.top;

            if (data.color === "rojo") {
                semaforo.src = "/static/punto-rojo.png";
            } else if (data.color === "verde") {
                semaforo.src = "/static/punto-verde.png";
            } else {
                semaforo.src = "/static/punto-gris.png";
            }
        });
}

atualizarPonto();
setInterval(atualizarPonto, 5000);
