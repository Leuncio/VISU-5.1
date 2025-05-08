from flask import Blueprint, jsonify
from .converciones import semaforo  # pode importar outros depois

js_bp = Blueprint('js', __name__)

@js_bp.route('/punto_rojo')
def get_semaforo():
    return jsonify(semaforo)