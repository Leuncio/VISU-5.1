document.addEventListener("DOMContentLoaded", function () {
    // Elementos principales
    const botonRuta = document.getElementById("botonRuta");
    const mapa = document.getElementById("mapa-img");
    const botaoMas = document.getElementById("botaoMas");
    const botaoMenos = document.getElementById("botaoMenos");
    const contador = document.getElementById("contador");

    // Verificación de elementos en el DOM
    if (!botonRuta || !mapa || !botaoMas || !botaoMenos || !contador) {
        console.error("Elemento no encontrado: Verifica que 'botonRuta', 'mapa-img', 'botaoMas', 'botaoMenos' y 'contador' existen en el HTML.");
        return;
    }

    let mostrandoRuta = false;
    let valorContador = 0;

    // Evento para cambiar la imagen del mapa
    botonRuta.addEventListener("click", function () {
        mostrandoRuta = !mostrandoRuta;
        console.log(`Botón presionado! Cambiando imagen a: ${mostrandoRuta ? "mapa-ruta.png" : "mapa.png"}`);
        mapa.src = mostrandoRuta ? "/static/mapa-ruta.png" : "/static/mapa.png";
    });

    // Evento para aumentar el contador de AVGs
    botaoMas.addEventListener("click", function () {
        valorContador++;
        contador.textContent = valorContador;
    });

    // Evento para disminuir el contador de AVGs (no permite valores negativos)
    botaoMenos.addEventListener("click", function () {
        if (valorContador > 0) {
            valorContador--;
            contador.textContent = valorContador;
        }
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

                    // Aplicar rotación si es un AGV
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
    "rojo": "/static/agv.svg",
    "azul": "/static/agv.svg",
    default: "/static/agv.svg"
};




function actualizarOrdenes() {
    fetch("/api/ordenes")
        .then(response => response.json())
        .then(ordenes => {
            const tablaOrdenes = document.getElementById("ordenes-container");
            tablaOrdenes.innerHTML = ""; // Limpiar tabla antes de actualizar

            ordenes.forEach(orden => {
                const fila = document.createElement("tr");
                fila.innerHTML = `
                    <th scope="row">${orden.id}</th>
                    <td>${orden.origen}</td>
                    <td>${orden.destino}</td>
                `;
                tablaOrdenes.appendChild(fila);  // Añadir nueva fila con datos actualizados
            });

            if (ordenes.length === 0) {
                tablaOrdenes.innerHTML = `<tr><td colspan="3">No hay órdenes registradas.</td></tr>`; // ✅ Mensaje si está vacío
            }
        })
        .catch(error => console.error("Error al actualizar órdenes:", error));
}

// 🚀 Actualización automática cada 5 segundos
setInterval(actualizarOrdenes, 5000);

// 🚀 Llamada inicial para cargar datos al abrir la página
actualizarOrdenes();






// Actualización automática cada 5 segundos
setInterval(() => atualizarElementos("/api/punto_semaforo", colorMappingSemaforos), 5000);
setInterval(() => atualizarElementos("/api/punto_avg", colorMappingAvgs, true), 5000);

// Llamada inicial para actualizar elementos
atualizarElementos("/api/punto_semaforo", colorMappingSemaforos);
atualizarElementos("/api/punto_avg", colorMappingAvgs, true);
