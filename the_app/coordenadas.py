from flask import current_app
from .converciones import obtener_elementos, dbs_para_listas

def load_data():
    """Load database values inside Flask's context dynamically."""
    with current_app.app_context():  # ✅ Ensures database queries run in a valid Flask context
        DB_NUMERO_SEMAFOROS, DB_COORDENADAS_SEMAFOROS_X, DB_COORDENADAS_SEMAFOROS_Y, DB_NUMERO_DE_AGVS, DB_COORDENADAS_AGVS_X, DB_COORDENADAS_AGVS_Y, DB_COORDENDAS_AGVS_A = dbs_para_listas()

    semaforos = obtener_elementos("semaforo", DB_COORDENADAS_SEMAFOROS_X, DB_COORDENADAS_SEMAFOROS_Y, [0] * DB_NUMERO_SEMAFOROS, DB_NUMERO_SEMAFOROS)
    agvs = obtener_elementos("agv", DB_COORDENADAS_AGVS_X, DB_COORDENADAS_AGVS_Y, DB_COORDENDAS_AGVS_A, DB_NUMERO_DE_AGVS)

    return semaforos, agvs  # ✅ Return instead of defining global variables



# Coordenadas manuales
# NUMERO_DE_SEMAFOROS = 14
# COORDENADAS_SEMAFOROS_X = [37.6, 32.57, 20.5, 37, 20.5, 21.2, 22.2, 22.28, 25.6, 27.09, 41.3, 22.81, 41.95, 17.55]
# COORDENADAS_SEMAFOROS_Y = [22.55, 22.77, 15.38, 20.7, 14.23, 12.5, 11.5, 13.14, 21.39, 16.52, 20.51, 7.15, 18.62, 12.11]
# NUMERO_DE_AGVS = 3  
# COORDENADAS_AGVS_X = [5, 6, 19]
# COORDENADAS_AGVS_Y = [5, 6, 7]
# COORDENDAS_AGVS_A = [45, 90, 135]  

# Obtener datos procesados con número correcto de semáforos
# semaforos = obtener_elementos("semaforo", COORDENADAS_SEMAFOROS_X, COORDENADAS_SEMAFOROS_Y, [0] * NUMERO_DE_SEMAFOROS, NUMERO_DE_SEMAFOROS)
# agvs = obtener_elementos("agv", COORDENADAS_AGVS_X, COORDENADAS_AGVS_Y, COORDENDAS_AGVS_A , NUMERO_DE_AGVS)


# print(semaforos)
# print(agvs)
