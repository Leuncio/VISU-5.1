# py_to_js.py

from flask import Blueprint, jsonify
from .converciones import (
    obtener_bits_salida,
    obtener_bits_entrada,
    dbs_para_dict,
    obtener_elementos,
    obtener_semaforos,
)

js_bp = Blueprint('js', __name__)


@js_bp.route('/punto_semaforo')
def get_semaforo():
    db = dbs_para_dict()
    entry = db.get("database_entry_gui", [{}])[0]
    semaforos_data = db.get("database_semaforos", [])
    
    elementos = obtener_semaforos(entry, semaforos_data)  # ← aqui sim usa os bits
    return jsonify(elementos)


@js_bp.route('/punto_agv')
def get_agv():
    db = dbs_para_dict()
    entry = db.get("database_entry_gui", [{}])[0]
    agvs = [i for i in range(1, 100) if f"X_AGV{i}" in entry]
    x = [entry[f"X_AGV{i}"] for i in agvs]
    y = [entry[f"Y_AGV{i}"] for i in agvs]
    a = [entry[f"A_AGV{i}"] for i in agvs]
    elementos = obtener_elementos("agv", x, y, angulo=a, num_elementos=len(agvs))
    return jsonify(elementos)

@js_bp.route('/ordenes')
def get_ordenes():
    ordenes = dbs_para_dict().get("database_ordenes", [])
    return jsonify(ordenes)


@js_bp.route('/estado_comunicaciones')
def get_estado_comunicaciones():
    db = dbs_para_dict()
    entry = db.get("database_entry_gui", [{}])[0]

    com = entry.get("COM", 0)
    agvs = [i for i in range(1, 100) if f"COM_AGV{i}" in entry]

    agv_estados = [
        {
            "id": f"AGV{i}",
            "status": entry.get(f"COM_AGV{i}", 0)
        } for i in agvs
    ]

    return jsonify({
        "plc": com,
        "agvs": agv_estados
    })



@js_bp.route('/inputs')
def get_inputs():
    db = dbs_para_dict()
    entry = db.get("database_entry_gui", [{}])[0]
    bits = obtener_bits_entrada(entry, llave="Inputs", num_bits=14)
    return jsonify(bits)

@js_bp.route('/outputs')
def get_outputs():
    db = dbs_para_dict()
    entry = db.get("database_entry_gui", [{}])[0]
    bits = obtener_bits_salida(entry, llave="Outputs", num_bits=4)
    return jsonify(bits)

@js_bp.route('/com')
def get_com():
    db = dbs_para_dict()
    entry = db.get("database_entry_gui", [{}])[0]
    com = entry.get("COM", 0)  # ← Isso em vez de entry.COM
    return jsonify({"COM": com})

