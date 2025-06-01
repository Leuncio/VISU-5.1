# views.py

from flask import Blueprint, render_template
from .coordenadas import semaforos, agvs
from .listas_on_off import comunicaciones
# Create a Blueprint for the main application
main_bp = Blueprint('main', __name__, template_folder='templates')  # Define blueprint with the name 'main'

@main_bp.route('/', methods=['GET', 'POST'])
def home():
    # map
    print(f"semaforo en el server: {semaforos}")
    print(f"avgs en el server: {agvs}")

    # listas_on_off
    print(comunicaciones)

    return render_template('index.html', semaforos=semaforos, agvs=agvs, comunicaciones=comunicaciones)