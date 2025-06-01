# views.py

from flask import Blueprint, render_template
from .coordenadas import semaforos, agvs
# Create a Blueprint for the main application
main_bp = Blueprint('main', __name__, template_folder='templates')  # Define blueprint with the name 'main'

@main_bp.route('/', methods=['GET', 'POST'])
def home():

    print(f"semaforo en el server: {semaforos}")
    print(f"avgs en el server: {agvs}")
    return render_template('index.html', semaforos=semaforos, agvs=agvs)