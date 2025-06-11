# de_setup

from the_app.models import db, DatabaseEntryGUI, DatabaseOrdenes, DatabaseOutGUI, DatabaseSemaforos
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


        # 🔹 Insere semáforos padrão se a tabela estiver vazia
        if not DatabaseSemaforos.query.first():
            default_semaforos = [
                DatabaseSemaforos(X=9.0, Y=7.0),
                DatabaseSemaforos(X=4.0, Y=3.0),
                DatabaseSemaforos(X=15.0, Y=10.0)  # Adiciona mais alguns exemplos
            ]
            db.session.add_all(default_semaforos)


        db.session.commit()  # Save changes
