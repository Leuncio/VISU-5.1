# views.py

from flask import Blueprint, render_template
from .converciones import dbs_para_dict, obtener_agvs, obtener_semaforos

# Criar o Blueprint principal
main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/', methods=['GET', 'POST'])
def home():
    db = dbs_para_dict()

    ordenes = db.get("database_ordenes", [])
    entry_data = db.get("database_entry_gui", [{}])[0]
    out_data = db.get("database_out_gui", [{}])[0]
    semaforos_data = db.get("database_semaforos", [])

    agvs = obtener_agvs(entry_data)
    semaforos = obtener_semaforos(semaforos_data)

    return render_template(
        'index.html',
        ordenes=ordenes,
        agvs=agvs,
        semaforos=semaforos,
        entradas=entry_data,
        salidas=out_data
    )
