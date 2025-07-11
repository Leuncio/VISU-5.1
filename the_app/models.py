# models.py

from flask import Flask
from sqlalchemy import create_engine, Integer, Float, String, Column
from sqlalchemy.orm import declarative_base, Session
import os

# Parámetros iniciales para la tabla de entrada
ENTRY_INPUTS = 2
ENTRY_OUTPUTS = 3
ENTRY_MENSAJES = "Mensaje de ejemplo"
ENTRY_BOTONES_IN = 9
SEMAFORO = 8
NUM_AGVS = 7  # máximo 10 AGVs
COM_DEFAULT = 1
AGV_DEFAULT_COM = 1
AGV_DEFAULT_X = 1.0
AGV_DEFAULT_Y = 1.0
AGV_DEFAULT_A = 1.0

# Parámetros para la tabla de órdenes
ORDEN_ORIGEN = "Origen A"
ORDEN_DESTINO = "Destino A"

# Parámetros para la tabla de salida
OUTGUI_NUM_BOTONES = 2
OUTGUI_NUMERO_AGVS = 0

# Parámetros para los semáforos
SEMAFORO_X = 30.0
SEMAFORO_Y = 18.0

# Inicializar la app y crear carpeta local de base de datos
app = Flask(__name__)
os.makedirs("instance", exist_ok=True)

# Declaración de bases de datos
BaseEntryGUI = declarative_base()
BaseOrdenes = declarative_base()
BaseOutGUI = declarative_base()
BaseSemaforos = declarative_base()

# Motores de conexión (uno por tabla)
engine_entry = create_engine("sqlite:///instance/database_entry_gui.db", echo=False)
engine_ordenes = create_engine("sqlite:///instance/database_ordenes.db", echo=False)
engine_out = create_engine("sqlite:///instance/database_out_gui.db", echo=False)
engine_semaforos = create_engine("sqlite:///instance/database_semaforos.db", echo=False)

# Modelo dinámico para entrada de datos (AGVs incluidos)
attrs = {
    '__tablename__': 'database_entry_gui',
    'id': Column(Integer, primary_key=True),
    'Inputs': Column(Integer, nullable=False, default=ENTRY_INPUTS),
    'Outputs': Column(Integer, nullable=False, default=ENTRY_OUTPUTS),
    'Mensajes': Column(String, nullable=False, default=ENTRY_MENSAJES),
    'Botones_in': Column(Integer, nullable=False, default=ENTRY_BOTONES_IN),
    'COM': Column(Integer, nullable=False, default=COM_DEFAULT),
    'Semaforo': Column(Integer, nullable=False, default=SEMAFORO),
}
for i in range(1, NUM_AGVS + 1):
    attrs[f'COM_AGV{i}'] = Column(Integer, nullable=False, default=AGV_DEFAULT_COM)
    attrs[f'X_AGV{i}'] = Column(Float, nullable=False, default=AGV_DEFAULT_X)
    attrs[f'Y_AGV{i}'] = Column(Float, nullable=False, default=AGV_DEFAULT_Y)
    attrs[f'A_AGV{i}'] = Column(Float, nullable=False, default=AGV_DEFAULT_A)
DatabaseEntryGUI = type('DatabaseEntryGUI', (BaseEntryGUI,), attrs)

# Modelo para órdenes
class DatabaseOrdenes(BaseOrdenes):
    __tablename__ = "database_ordenes"
    id = Column(Integer, primary_key=True)
    origen = Column(String, nullable=False, default=ORDEN_ORIGEN)
    destino = Column(String, nullable=False, default=ORDEN_DESTINO)

# Modelo para salida GUI
class DatabaseOutGUI(BaseOutGUI):
    __tablename__ = "database_out_gui"
    id = Column(Integer, primary_key=True)
    numero_agvs = Column(Integer, nullable=False, default=OUTGUI_NUMERO_AGVS)
    botones_out = Column(Integer, nullable=False, default=OUTGUI_NUM_BOTONES)

# Modelo para semáforos
class DatabaseSemaforos(BaseSemaforos):
    __tablename__ = "database_semaforos"
    id = Column(Integer, primary_key=True)
    X = Column(Float, nullable=False, default=SEMAFORO_X)
    Y = Column(Float, nullable=False, default=SEMAFORO_Y)

# Crear las tablas si no existen (no las borra)
BaseEntryGUI.metadata.create_all(engine_entry)
BaseOrdenes.metadata.create_all(engine_ordenes)
BaseOutGUI.metadata.create_all(engine_out)
BaseSemaforos.metadata.create_all(engine_semaforos)

# Insertar valores por defecto si la tabla está vacía
with Session(engine_entry) as session:
    if session.query(DatabaseEntryGUI).count() == 0:
        session.add(DatabaseEntryGUI())
        session.commit()

with Session(engine_ordenes) as session:
    if session.query(DatabaseOrdenes).count() == 0:
        session.add(DatabaseOrdenes())
        session.commit()

with Session(engine_out) as session:
    if session.query(DatabaseOutGUI).count() == 0:
        session.add(DatabaseOutGUI())
        session.commit()

with Session(engine_semaforos) as session:
    if session.query(DatabaseSemaforos).count() == 0:
        session.add(DatabaseSemaforos())
        session.commit()

# Función para convertir las tablas en diccionarios utilizables por la lógica de la app
def dbs_para_dict():
    resultados = {}

    with Session(engine_entry) as session:
        entry_rows = session.query(DatabaseEntryGUI).all()
        resultados['database_entry_gui'] = [row.__dict__.copy() for row in entry_rows]

    with Session(engine_ordenes) as session:
        ordenes_rows = session.query(DatabaseOrdenes).all()
        resultados['database_ordenes'] = [row.__dict__.copy() for row in ordenes_rows]

    with Session(engine_out) as session:
        out_rows = session.query(DatabaseOutGUI).all()
        resultados['database_out_gui'] = [row.__dict__.copy() for row in out_rows]

    with Session(engine_semaforos) as session:
        semaforos_rows = session.query(DatabaseSemaforos).all()
        resultados['database_semaforos'] = [row.__dict__.copy() for row in semaforos_rows]

    # Eliminar la clave interna de SQLAlchemy (_sa_instance_state)
    for key in resultados:
        for item in resultados[key]:
            item.pop('_sa_instance_state', None)

    return resultados
