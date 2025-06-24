# views

from flask import Blueprint, render_template
from .coordenadas import load_data
from the_app.models import DatabaseOrdenes
from flask import current_app

# Crear el Blueprint
main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/', methods=['GET', 'POST'])
def home():
    with current_app.app_context():  # Asegurar contexto de Flask
        ordenes = DatabaseOrdenes.query.all()  # 🔹 Obtener órdenes desde la DB

    semaforos, agvs = load_data()  

    return render_template('index.html', semaforos=semaforos, agvs=agvs, ordenes=ordenes)
