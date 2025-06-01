# coordenadas.py

# Este archivo contiene funciones para convertir coordenadas de metros a porcentajes CSS
from .converciones import metros_a_css_porcentaje, numero_para_lista_binaria

NUMERO_DE_SEMAFOROS = 5
NUMERO_DE_AGVS = 3  # Puedes ajustar el número de AGVs según lo necesites

def obtener_elementos(tipo, x, y, num_elementos):
    """
    Obtiene las coordenadas de los elementos en formato CSS,
    asignando un único bit a cada uno.
    """
    elementos = []
    binario = numero_para_lista_binaria(num_elementos)

    for i in range(num_elementos):
        elemento = metros_a_css_porcentaje(x, y)
        elemento["color"] = binario[i % len(binario)]  # Atribuye un único bit
        elemento["id"] = f"{tipo}-{i}"
        elementos.append(elemento)

    return elementos

# Obtener semáforos y AGVs
semaforos = obtener_elementos("semaforo", 6, 6, NUMERO_DE_SEMAFOROS)
agvs = obtener_elementos("agv", 5, 5, NUMERO_DE_AGVS)

print(semaforos)
print(agvs)
