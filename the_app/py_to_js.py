from flask import Blueprint, jsonify
from .coordenadas import load_data

js_bp = Blueprint('js', __name__)

@js_bp.route('/punto_semaforo')
def get_semaforo():
    semaforos, _ = load_data()
    return jsonify(semaforos)

@js_bp.route('/punto_avg')
def get_avg():
    _, agvs = load_data()
    return jsonify(agvs)
