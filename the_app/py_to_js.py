from flask import Blueprint, jsonify
from .coordenadas import load_data
from the_app.models import DatabaseOrdenes
from flask import current_app

js_bp = Blueprint('js', __name__)

@js_bp.route('/punto_semaforo')
def get_semaforo():
    semaforos, _ = load_data()
    return jsonify(semaforos)

@js_bp.route('/punto_avg')
def get_avg():
    _, agvs = load_data()
    return jsonify(agvs)

@js_bp.route('/ordenes')
def get_ordenes():
    with current_app.app_context():
        ordenes = DatabaseOrdenes.query.all()
        ordenes_json = [{"id": o.id, "origen": o.origen, "destino": o.destino} for o in ordenes]  # 🔹 Formateo JSON
    return jsonify(ordenes_json)
