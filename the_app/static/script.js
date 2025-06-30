document.addEventListener("DOMContentLoaded", function () {
    const botonRuta = document.getElementById("botonRuta");
    const mapa = document.getElementById("mapa-img");
    const botaoMas = document.getElementById("botaoMas");
    const botaoMenos = document.getElementById("botaoMenos");
    const contador = document.getElementById("contador");

    if (!botonRuta || !mapa || !botaoMas || !botaoMenos || !contador) {
        console.error("Elemento não encontrado: Verifique os IDs no HTML.");
        return;
    }

    let mostrandoRuta = false;
    let valorContador = parseInt(contador.textContent.trim()) || 0;

    botonRuta.addEventListener("click", function () {
        mostrandoRuta = !mostrandoRuta;
        mapa.src = mostrandoRuta
            ? "/static/mapa-ruta.png"
            : "/static/mapa.png";
    });

    botaoMas.addEventListener("click", function () {
        valorContador++;
        contador.textContent = valorContador;
    });

    botaoMenos.addEventListener("click", function () {
        if (valorContador > 0) {
            valorContador--;
            contador.textContent = valorContador;
        }
    });
});


function actualizarElementos(url, colorMapping = {}, includeRotation = false) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            data.forEach(info => {
                const el = document.getElementById(info.id);
                if (!el) return;

                el.style.left = info.left;
                el.style.top = info.top;

                if (colorMapping && info.color !== undefined) {
                    el.src = colorMapping[info.color] || colorMapping.default;
                }

                if (includeRotation && info.angulo !== undefined) {
                    el.style.transform = `translate(-50%, -50%) rotate(${info.angulo}deg)`;
                }
            });
        })
        .catch(err => console.error("Erro ao actualizar elementos:", err));
}


function actualizarSemaforos(url) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            data.forEach(info => {
                const el = document.getElementById(info.id);
                if (!el) return;

                // actualizar a cor da imagem com base no valor binário
                el.src = info.color === 1
                    ? "/static/punto-verde.png"
                    : "/static/punto-rojo.png";

                // Atualiza posição também (opcional)
                el.style.left = info.left;
                el.style.top = info.top;
            });
        })
        .catch(err => console.error("Erro ao actualizar semáforos:", err));
}


function actualizarOrdenes() {
    fetch("/api/ordenes")
        .then(res => res.json())
        .then(ordenes => {
            const tbody = document.getElementById("ordenes-container");
            tbody.innerHTML = "";

            if (ordenes.length === 0) {
                tbody.innerHTML = `<tr><td colspan="3">No hay órdenes registradas.</td></tr>`;
                return;
            }

            ordenes.forEach(o => {
                tbody.innerHTML += `
                    <tr>
                        <th scope="row">${o.id}</th>
                        <td>${o.origen}</td>
                        <td>${o.destino}</td>
                    </tr>
                `;
            });
        })
        .catch(err => console.error("Erro ao buscar órdenes:", err));
}



function actualizarComunicaciones() {
    fetch("/api/estado_comunicaciones", { cache: "no-store" })
        .then(res => res.json())
        .then(data => {
            const plc = document.getElementById("plc-status");
            if (plc) {
                plc.src = data.plc === 1
                    ? "/static/punto-verde.png"
                    : "/static/punto-rojo.png";
            }

            const container = document.getElementById("estado-agvs");
            if (container) {
                container.innerHTML = "";
                data.agvs.forEach((agv, index) => {
                    const etiqueta = document.createElement("span");
                    etiqueta.className = "etiqueta";
                    etiqueta.textContent = `${agv.id}:`;

                    const imagen = document.createElement("img");
                    imagen.className = "entrada-bit";  // mesmo estilo dos outros puntos
                    imagen.src = agv.status === 1
                        ? "/static/punto-verde.png"
                        : "/static/punto-rojo.png";

                    // Inserir: AGVx: <punto> [espaço]
                    container.appendChild(etiqueta);
                    container.appendChild(imagen);
                    container.appendChild(document.createTextNode(" "));  // ← espaço depois do ponto
                });
            }
        })
        .catch(err => console.error("Error al actualizar comunicaciones:", err));
}




function checkCom() {
    fetch("/api/com")
        .then(res => res.json())
        .then(data => {
            const com = data.COM;

            if (com === 1) {
                actualizarEntradas();
                actualizarSalidas();
            } else {
                fetch("/api/inputs")
                    .then(res => res.json())
                    .then(bits => {
                        bits.forEach((bit, index) => {
                            const img = document.querySelector(`.entrada-bit[data-entrada="${index}"]`);
                            if (img) {
                                img.src = "/static/punto-gris.png";
                            }
                        });
                    })
                    .catch(err => console.error("Erro ao forçar cinza nas entradas:", err));

                document.querySelectorAll(".salida-bit").forEach(img => {
                    img.src = "/static/punto-gris.png";
                });

                const plc = document.getElementById("plc-status");
                if (plc) plc.src = "/static/punto-rojo.png";
            }
        })
        .catch(err => console.error("Erro ao verificar COM:", err));
}





function actualizarEntradas() {
    fetch("/api/inputs")
        .then(res => res.json())
        .then(bits => {
            bits.forEach((bit, index) => {
                const img = document.querySelector(`.entrada-bit[data-entrada="${index}"]`);
                if (img) {
                    img.src = bit === 1
                        ? "/static/punto-verde.png"
                        : "/static/punto-rojo.png";
                }
            });
        })
        .catch(err => console.error("Erro ao actualizar entradas:", err));
}


function actualizarSalidas() {
    fetch("/api/outputs")  // ← correto agora
        .then(res => res.json())
        .then(bits => {
            bits.forEach((bit, index) => {
                const img = document.querySelector(`.salida-bit[data-salida="${index}"]`);
                if (img) {
                    img.src = bit === 1
                        ? "/static/punto-verde.png"
                        : "/static/punto-rojo.png";
                }
            });
        })
        .catch(err => console.error("Erro ao actualizar salidas:", err));
}



const colorMappingSemaforos = {
    0: "/static/punto-rojo.png",
    1: "/static/punto-verde.png",
    default: "/static/punto-gris.png"
};

const colorMappingAgvs = {
    default: "/static/agv.svg"
};

setInterval(actualizarOrdenes, 5000);
setInterval(() => actualizarElementos("/api/punto_agv", colorMappingAgvs, true), 5000);
setInterval(checkCom, 2000);
setInterval(() => actualizarSemaforos("/api/punto_semaforo"), 5000);
setInterval(actualizarComunicaciones, 3000);

actualizarOrdenes();
actualizarElementos("/api/punto_agv", colorMappingAgvs, true);
actualizarSemaforos("/api/punto_semaforo");
actualizarComunicaciones();

checkCom;
