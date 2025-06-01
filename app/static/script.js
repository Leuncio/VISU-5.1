// script.js


// map
   

// semaforos
const semaforo = document.getElementById("punto-semaforo");

function atualizarSemaforo() {
    fetch("/api/punto_semaforo")
        .then(response => response.json())
        .then(data => {
            data.forEach(semaforoInfo => {
                const semaforo = document.getElementById(semaforoInfo.id);
                if (semaforo) {
                    semaforo.style.left = semaforoInfo.left;
                    semaforo.style.top = semaforoInfo.top;
                    
                    if (semaforoInfo.color === 0) {
                        semaforo.src = "/static/punto-rojo.png";
                    } else if (semaforoInfo.color === 1) {
                        semaforo.src = "/static/punto-verde.png";
                    } else {
                        semaforo.src = "/static/punto-gris.png";
                    }
                }
            });
        });
}

atualizarSemaforo();
setInterval(atualizarSemaforo, 5000);

// avgs
const avg = document.getElementById("punto-avg");

function atualizarAvg() {
    fetch("/api/punto_avg")
        .then(response => response.json())
        .then(data => {
            avg.style.left = data.left;
            avg.style.top = data.top;

            if (data.color === "rojo") {
                avg.src = "/static/agv-rojo.png";
            } else if (data.color === "azul") {
                avg.src = "/static/agv-azul.png";
            } else {
                avg.src = "/static/agv-rojo.png";
            }
        });
}

atualizarAvg();
setInterval(atualizarAvg, 5000);



