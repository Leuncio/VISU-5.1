from flask import Blueprint, jsonify
from .coordenadas import semaforos, agvs  # pode importar outros depois

js_bp = Blueprint('js', __name__)

@js_bp.route('/punto_semaforo')
def get_semaforo():
    return jsonify(semaforos)

@js_bp.route('/punto_avg')
def get_avg():
    return jsonify(agvs)