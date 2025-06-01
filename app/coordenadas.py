# Este archivo contiene funciones para convertir coordenadas de metros a porcentajes CSS
from .converciones import metros_a_css_porcentaje, numero_para_lista_binaria

NUMERO_DE_SEMAFOROS = 5
NUMERO_DE_AGVS = 3  # Puedes ajustar el número de AGVs según lo necesites

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
coordenadas_semaforos_x = [6, 7, 8, 9, 10]
coordenadas_semaforos_y = [6, 7, 8, 9, 10]

coordenadas_agvs_x = [5, 6, 7]
coordenadas_agvs_y = [5, 6, 7]
angulos_agvs = [45, 90, 135]  # Definir manualmente los ángulos

# Obtener semáforos y AGVs con coordenadas específicas
semaforos = obtener_elementos("semaforo", coordenadas_semaforos_x, coordenadas_semaforos_y, [0] * NUMERO_DE_SEMAFOROS, NUMERO_DE_SEMAFOROS)
agvs = obtener_elementos("agv", coordenadas_agvs_x, coordenadas_agvs_y, angulos_agvs, NUMERO_DE_AGVS)

print(semaforos)
print(agvs)
