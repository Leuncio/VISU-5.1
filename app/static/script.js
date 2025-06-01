document.addEventListener("DOMContentLoaded", function () {
    const botonRuta = document.getElementById("botonRuta");
    const mapa = document.getElementById("mapa-img");

    if (!botonRuta || !mapa) {
        console.error("Elemento no encontrado: Verifica que 'botonRuta' y 'mapa-img' existen en el HTML.");
        return;
    }

    let mostrandoRuta = false;

    botonRuta.addEventListener("click", function () {
        mostrandoRuta = !mostrandoRuta;
        console.log(`Botón presionado! Cambiando imagen a: ${mostrandoRuta ? "mapa-ruta.png" : "mapa.png"}`);
        mapa.src = mostrandoRuta ? "/static/mapa-ruta.png" : "/static/mapa.png";
    });
});

// Función para actualizar semáforos y AGVs
function atualizarElementos(url, colorMapping, includeRotation = false) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            data.forEach(elementoInfo => {
                const elemento = document.getElementById(elementoInfo.id);
                if (elemento) {
                    elemento.style.left = elementoInfo.left;
                    elemento.style.top = elementoInfo.top;
                    elemento.src = colorMapping[elementoInfo.color] || colorMapping["default"];

                    if (includeRotation && elementoInfo.angulo !== undefined) {
                        elemento.style.transform = `translate(-50%, -50%) rotate(${elementoInfo.angulo}deg)`;
                    }
                }
            });
        })
        .catch(error => console.error("Error al actualizar elementos:", error));
}

// Mapeo de imágenes para semáforos
const colorMappingSemaforos = {
    0: "/static/punto-rojo.png",
    1: "/static/punto-verde.png",
    default: "/static/punto-gris.png"
};

// Mapeo de imágenes para AGVs
const colorMappingAvgs = {
    "rojo": "/static/agv-rojo.png",
    "azul": "/static/agv-azul.png",
    default: "/static/agv-rojo.png"
};

// Actualización automática cada 5 segundos
setInterval(() => atualizarElementos("/api/punto_semaforo", colorMappingSemaforos), 5000);
setInterval(() => atualizarElementos("/api/punto_avg", colorMappingAvgs, true), 5000);

// Llamada inicial para actualizar elementos
atualizarElementos("/api/punto_semaforo", colorMappingSemaforos);
atualizarElementos("/api/punto_avg", colorMappingAvgs, true);
