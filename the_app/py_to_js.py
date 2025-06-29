# py_to_js.py

from .converciones import dbs_para_dict, obtener_elementos
from flask import Blueprint, jsonify

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

@js_bp.route('/entrada_out')
def get_entrada_out():
    entrada = dbs_para_dict().get("database_entry_gui", [])
    return jsonify(entrada)

@js_bp.route('/salida_out')
def get_salida_out():
    salida = dbs_para_dict().get("database_out_gui", [])
    return jsonify(salida)




