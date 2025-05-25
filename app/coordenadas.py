# coordenadas.py

# This file contains functions for converting coordinates from meters to CSS percentage values
from converciones import metros_a_css_porcentaje, numero_para_lista_binaria

NUMERO_DE_SEMAFOFOS = 5

def obtener_semaforo(x, y, num_semaforos=NUMERO_DE_SEMAFOFOS):
    """
    Obtiene las coordenadas del semáforo en formato CSS,
    asignando un único bit a cada semáforo.
    """
    semaforos = []
    binario = numero_para_lista_binaria(NUMERO_DE_SEMAFOFOS)

    for i in range(num_semaforos):
        semaforo = metros_a_css_porcentaje(x, y)
        semaforo["color"] = binario[i % len(binario)]  # Atribui um único bit
        semaforo["id"] = f"semaforo-{i}"
        semaforos.append(semaforo)

    return semaforos


semaforo = obtener_semaforo(10, 20)
print (semaforo)