# coordenadas.py

from .converciones import metros_a_css_porcentaje, numero_para_lista_binaria, obtener_elementos

# Coordenadas definidas manualmente
NUMERO_DE_SEMAFOROS = 5
COORDENADAS_SEMAFOROS_X = [6, 7, 8, 9, 10]
COORDENADAS_SEMAFOROS_Y = [6, 7, 8, 9, 10]
NUMERO_DE_AGVS = 3  # Puedes ajustar el número de AGVs según lo necesites
COORDENADAS_AGVS_X = [5, 6, 19]
COORDENADAS_AGVS_Y = [5, 6, 7]
COORDENDAS_AGVS_A = [45, 90, 135]  # Definir manualmente los ángulos


# Coordenadas definidas manualmente

# Obtener semáforos y AGVs con coordenadas específicas
semaforos = obtener_elementos("semaforo", COORDENADAS_SEMAFOROS_X, COORDENADAS_SEMAFOROS_Y, [0] * NUMERO_DE_SEMAFOROS, NUMERO_DE_SEMAFOROS)
agvs = obtener_elementos("agv", COORDENADAS_AGVS_X, COORDENADAS_AGVS_Y, COORDENDAS_AGVS_A , NUMERO_DE_AGVS)

print(semaforos)
print(agvs)
