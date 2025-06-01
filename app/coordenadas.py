# Este archivo contiene funciones para convertir coordenadas de metros a porcentajes CSS
from .converciones import metros_a_css_porcentaje, numero_para_lista_binaria

# Coordenadas definidas manualmente
NUMERO_DE_SEMAFOROS = 5
COORDENADAS_SEMAFOROS_X = [6, 7, 8, 9, 10]
COORDENADAS_SEMAFOROS_Y = [6, 7, 8, 9, 10]
NUMERO_DE_AGVS = 3  # Puedes ajustar el número de AGVs según lo necesites
COORDENADAS_AGVS_X = [5, 6, 19]
COORDENADAS_AGVS_Y = [5, 6, 7]
COORDENDAS_AGVS_A = [45, 90, 135]  # Definir manualmente los ángulos


def obtener_elementos(tipo, x, y, angulo, num_elementos):
    """
    Obtiene las coordenadas de los elementos en formato CSS,
    asignando un único bit a cada uno. Permite definir X, Y y el ángulo para AGVs.
    """
    elementos = []
    binario = numero_para_lista_binaria(num_elementos)

    for i in range(num_elementos):
        elemento = metros_a_css_porcentaje(x[i], y[i])  # Usa listas para definir posiciones individuales
        elemento["color"] = binario[i % len(binario)]  # Atribuye un único bit
        elemento["id"] = f"{tipo}-{i}"

        # Si el elemento es un AGV, agregar el ángulo definido
        if tipo == "agv":
            elemento["angulo"] = angulo[i]  # Se pasa el ángulo desde la lista

        elementos.append(elemento)

    return elementos

# Coordenadas definidas manualmente

# Obtener semáforos y AGVs con coordenadas específicas
semaforos = obtener_elementos("semaforo", COORDENADAS_SEMAFOROS_X, COORDENADAS_SEMAFOROS_Y, [0] * NUMERO_DE_SEMAFOROS, NUMERO_DE_SEMAFOROS)
agvs = obtener_elementos("agv", COORDENADAS_AGVS_X, COORDENADAS_AGVS_Y, COORDENDAS_AGVS_A , NUMERO_DE_AGVS)

print(semaforos)
print(agvs)
