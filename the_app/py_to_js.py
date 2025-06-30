# py_to_js.py

from flask import Blueprint, jsonify
from .converciones import obtener_bits_entrada, obtener_bits_salida  # certifique-se de importar isso
from .converciones import (
    dbs_para_dict,
    obtener_elementos,
)


js_bp = Blueprint('js', __name__)

@js_bp.route('/punto_semaforo')
def get_semaforo():
    db = dbs_para_dict()
    semaforos = db.get("database_semaforos", [])
    x = [s["X"] for s in semaforos]
    y = [s["Y"] for s in semaforos]
    n = len(semaforos)
    elementos = obtener_elementos("semaforo", x, y, angulo=[0]*n, num_elementos=n)
    return jsonify(elementos)

@js_bp.route('/punto_avg')
def get_avg():
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

