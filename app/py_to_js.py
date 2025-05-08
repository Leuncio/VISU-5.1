from flask import Blueprint, jsonify
from .converciones import punto_rojo  # pode importar outros depois

js_bp = Blueprint('js', __name__)

@js_bp.route('/punto_rojo')
def get_punto_rojo():
    return jsonify(punto_rojo)