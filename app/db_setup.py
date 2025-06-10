# de_setup

from app.models import db, DatabaseEntryGUI, DatabaseOrdenes, DatabaseOutGUI
from flask import current_app

def insert_default_data():
    with current_app.app_context():
        db.create_all()

        # 🔹 Ensure at least one entry exists in DatabaseEntryGUI
        if not DatabaseEntryGUI.query.first():
            default_entry_gui = DatabaseEntryGUI(AVG=1.0, X=1.0, Y=1.0, A=1.0)  # Explicitly insert default values
            db.session.add(default_entry_gui)

        # 🔹 Insert default values into DatabaseOrdenes
        if not DatabaseOrdenes.query.first():
            default_ordenes = [
                DatabaseOrdenes(origen=f"Origen {chr(65+i)}", destino=f"Destino {chr(65+i)}") for i in range(7)
            ]
            db.session.add_all(default_ordenes)

        # 🔹 Insert default values into DatabaseOutGUI
        if not DatabaseOutGUI.query.first():
            default_out_gui = DatabaseOutGUI(numero_agvs=1, out_botones=0)
            db.session.add(default_out_gui)

        db.session.commit()  # Save changes
