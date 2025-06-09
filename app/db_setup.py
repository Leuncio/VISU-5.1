# de_setup

# db_setup.py
from app.models import db, DatabaseOrdenes, DatabaseOutGUI
from flask import current_app

from app.models import db, DatabaseOrdenes, DatabaseOutGUI
from flask import current_app

def insert_default_data():
    with current_app.app_context():  # ✅ Ensures Flask context is active
        db.create_all()

        if not DatabaseOrdenes.query.first():
            default_ordenes = [
                DatabaseOrdenes(origen=f"Origen {chr(65+i)}", destino=f"Destino {chr(65+i)}") for i in range(7)
            ]
            db.session.add_all(default_ordenes)

        if not DatabaseOutGUI.query.first():
            default_out_gui = DatabaseOutGUI(numero_agvs=1, out_botones=0)
            db.session.add(default_out_gui)

        db.session.commit()

