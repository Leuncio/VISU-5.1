# views.py

from flask import Blueprint, render_template
from .coordenadas import load_data  # ✅ Import function instead of variables
from .listas_on_off import comunicaciones

# Create a Blueprint for the main application
main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/', methods=['GET', 'POST'])
def home():
    # 🚀 Load database data dynamically inside the request
    semaforos, agvs = load_data()  

    # Debugging info
    print(f"semaforo en el server: {semaforos}")
    print(f"avgs en el server: {agvs}")
    print(comunicaciones)

    return render_template('index.html', semaforos=semaforos, agvs=agvs, comunicaciones=comunicaciones)
