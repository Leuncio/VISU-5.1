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


function atualizarElementos(url, colorMapping = {}, includeRotation = false) {
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
        .catch(err => console.error("Erro ao atualizar elementos:", err));
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


function atualizarEntradas() {
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
        .catch(err => console.error("Erro ao atualizar entradas:", err));
}


function atualizarSalidas() {
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
        .catch(err => console.error("Erro ao atualizar salidas:", err));
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
setInterval(() => atualizarElementos("/api/punto_semaforo", colorMappingSemaforos), 5000);
setInterval(() => atualizarElementos("/api/punto_avg", colorMappingAgvs, true), 5000);
setInterval(atualizarEntradas, 2000);
setInterval(atualizarSalidas, 2000);

actualizarOrdenes();
atualizarElementos("/api/punto_semaforo", colorMappingSemaforos);
atualizarElementos("/api/punto_avg", colorMappingAgvs, true);
atualizarEntradas();
atualizarSalidas();
