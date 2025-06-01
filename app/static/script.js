function atualizarElementos(url, claseElemento, colorMapping, includeRotation = false) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            data.forEach(elementoInfo => {
                const elemento = document.getElementById(elementoInfo.id);
                if (elemento) {
                    elemento.style.left = elementoInfo.left;
                    elemento.style.top = elementoInfo.top;

                    // Actualiza el color según el mapeo definido
                    elemento.src = colorMapping[elementoInfo.color] || colorMapping["default"];

                    // Si el elemento tiene un ángulo, aplicar la rotación CSS
                    if (includeRotation && elementoInfo.angulo !== undefined) {
                        elemento.style.transform = `translate(-50%, -50%) rotate(${elementoInfo.angulo}deg)`;
                    }
                }
            });
        });
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

// Llamadas a la función genérica
setInterval(() => atualizarElementos("/api/punto_semaforo", "semaforo", colorMappingSemaforos), 5000);
setInterval(() => atualizarElementos("/api/punto_avg", "avg", colorMappingAvgs, true), 5000);

// Llamada inicial para actualizar elementos desde el inicio
atualizarElementos("/api/punto_semaforo", "semaforo", colorMappingSemaforos);
atualizarElementos("/api/punto_avg", "avg", colorMappingAvgs, true);
