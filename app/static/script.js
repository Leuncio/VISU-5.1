// script.js


// map
   

// semaforos
const semaforo = document.getElementById("punto-semaforo");

function atualizarSemaforo() {
    fetch("/api/punto_semaforo")
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

atualizarSemaforo();
setInterval(atualizarSemaforo, 5000);



