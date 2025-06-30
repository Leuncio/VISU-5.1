# converciones.py

from flask import current_app
from .models import (
    engine_entry, engine_ordenes, engine_out, engine_semaforos,
    DatabaseEntryGUI, DatabaseOrdenes, DatabaseOutGUI, DatabaseSemaforos
)
from sqlalchemy.orm import Session

# Escala: 1 pixel = 0.05 metros
ESCALA_METROS_POR_PIXEL = 0.05

# Dimensiones reales del mapa en metros (basadas en el tamaño de la imagen en píxeles)
ANCHO_MAPA_M = 979 * ESCALA_METROS_POR_PIXEL  # 48.95 metros
ALTO_MAPA_M = 599 * ESCALA_METROS_POR_PIXEL  # 29.95 metros


def metros_a_css_porcentaje(x, y):
    """
    Convierte coordenadas (x, y) en metros a porcentaje CSS,
    basada en el tamaño del mapa y el sistema de coordenadas invertido del CSS.
    """
    x = min(max(x, 0), ANCHO_MAPA_M)
    y = min(max(y, 0), ALTO_MAPA_M)

    left_pct = (x / ANCHO_MAPA_M) * 100
    top_pct = ((ALTO_MAPA_M - y) / ALTO_MAPA_M) * 100  # Inversión del eje Y

    return {
        "left": f"{left_pct:.2f}%",
        "top": f"{top_pct:.2f}%"
    }


def dbs_para_dict():
    resultados = {}

    with Session(engine_entry) as session:
        entry_rows = session.query(DatabaseEntryGUI).all()
        resultados['database_entry_gui'] = [row.__dict__.copy() for row in entry_rows]

    with Session(engine_ordenes) as session:
        ordenes_rows = session.query(DatabaseOrdenes).all()
        resultados['database_ordenes'] = [row.__dict__.copy() for row in ordenes_rows]

    with Session(engine_out) as session:
        out_rows = session.query(DatabaseOutGUI).all()
        resultados['database_out_gui'] = [row.__dict__.copy() for row in out_rows]

    with Session(engine_semaforos) as session:
        semaforos_rows = session.query(DatabaseSemaforos).all()
        resultados['database_semaforos'] = [row.__dict__.copy() for row in semaforos_rows]

    # Remover chaves técnicas como '_sa_instance_state'
    for key in resultados:
        for item in resultados[key]:
            item.pop('_sa_instance_state', None)

    return resultados


def obtener_elementos(tipo, x, y, angulo, num_elementos):
    """
    Obtiene las coordenadas de los elementos en formato CSS,
    asignando ID y propiedades específicas para AGVs y semáforos.
    """
    elementos = []
    binario = numero_para_bits(num_elementos)  # ← útil se quiser usar bits depois

    for i in range(num_elementos):
        elemento = metros_a_css_porcentaje(x[i], y[i])

        if tipo == "agv":
            elemento["id"] = f"agv-{i + 1}"
            elemento["imagen"] = f"agv-{i + 1}.svg"
            elemento["angulo"] = angulo[i]
        elif tipo == "semaforo":
            elemento["id"] = f"semaforo-{i + 1}"
            # Aqui você pode adicionar imagem/filtro se quiser

        elementos.append(elemento)

    return elementos



def obtener_agvs(entry_data):
    """
    Procesa los datos de DatabaseEntryGUI para obtener los AGVs en formato CSS.
    """
    agvs_idx = [i for i in range(1, 100) if f"X_AGV{i}" in entry_data]
    x = [entry_data[f"X_AGV{i}"] for i in agvs_idx]
    y = [entry_data[f"Y_AGV{i}"] for i in agvs_idx]
    a = [entry_data[f"A_AGV{i}"] for i in agvs_idx]

    return obtener_elementos("agv", x, y, angulo=a, num_elementos=len(agvs_idx))


def obtener_semaforos(semaforos_data):
    """
    Procesa los datos de DatabaseSemaforos para obtener semáforos en formato CSS.
    """
    x = [s["X"] for s in semaforos_data]
    y = [s["Y"] for s in semaforos_data]
    num = len(semaforos_data)

    return obtener_elementos("semaforo", x, y, angulo=[0]*num, num_elementos=num)


def numero_para_bits(valor, num_bits=8):
    """
    Converte um inteiro em uma lista de bits (0 ou 1), com tamanho fixo.
    """
    binario = bin(valor)[2:].zfill(num_bits)
    return [int(b) for b in binario[-num_bits:]]


def obtener_bits_entrada(entry_data, llave="Inputs", num_bits=13):
    """
    Extrai bits do campo de entrada da base de dados.
    """
    valor = entry_data.get(llave, 0)
    return numero_para_bits(valor, num_bits)


def obtener_bits_salida(entry_data, llave="Outputs", num_bits=4):
    """
    Extrai bits do campo de saída da base de dados.
    """
    valor = entry_data.get(llave, 0)
    return numero_para_bits(valor, num_bits)


def obtener_bits_semaforos(semaforos_data, llave="Estados", num_bits=14):
    """
    Converte um valor (ou soma de flags) de semáforos em lista de bits.
    """
    if not semaforos_data:
        return [0] * num_bits

    valor = semaforos_data[0].get(llave, 0)
    return numero_para_bits(valor, num_bits)


