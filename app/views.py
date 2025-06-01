# views.py

from flask import Blueprint, render_template
from .coordenadas import semaforos, avg

# Create a Blueprint for the main application
main_bp = Blueprint('main', __name__, template_folder='templates')  # Define blueprint with the name 'main'

@main_bp.route('/', methods=['GET', 'POST'])
def home():

    print(f"semaforo en el server: {semaforos}")
    return render_template('index.html', semaforos=semaforos, avg=avg)