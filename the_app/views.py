# views.py

from flask import Blueprint, render_template
from .converciones import (
    dbs_para_dict,
    obtener_elementos,
    obtener_semaforos,
    obtener_bits_entrada,
    obtener_bits_salida,
)

# Criar o Blueprint principal
main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/', methods=['GET', 'POST'])
def home():
    db = dbs_para_dict()

    ordenes = db.get("database_ordenes", [])
    entry_data = db.get("database_entry_gui", [{}])[0]
    out_data = db.get("database_out_gui", [{}])[0]
    semaforos_data = db.get("database_semaforos", [])

    # Extrair dados dos AGVs do banco
    agvs_idx = [i for i in range(1, 100) if f"X_AGV{i}" in entry_data]
    x = [entry_data[f"X_AGV{i}"] for i in agvs_idx]
    y = [entry_data[f"Y_AGV{i}"] for i in agvs_idx]
    a = [entry_data[f"A_AGV{i}"] for i in agvs_idx]

    agvs = obtener_elementos("agv", x, y, angulo=a, num_elementos=len(agvs_idx))
    semaforos = obtener_semaforos(semaforos_data)
    entradas_bits = obtener_bits_entrada(entry_data, llave="Inputs", num_bits=13)
    salidas_bits = obtener_bits_salida(entry_data, llave="Outputs", num_bits=4)

    return render_template(
        'index.html',
        ordenes=ordenes,
        agvs=agvs,
        semaforos=semaforos,
        entradas=entry_data,
        salidas=out_data,
        entradas_bits=entradas_bits,
        salidas_bits=salidas_bits
    )
