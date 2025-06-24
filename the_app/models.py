from flask import Flask
from sqlalchemy import create_engine, Integer, Float, String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, Session
import os

# 🔧 Configurable parameters
NUM_AGVS = 5
AGV_DEFAULT_NAME = "AGV"
AGV_DEFAULT_X = 1.0
AGV_DEFAULT_Y = 1.0

ENTRY_INPUTS = 2
ENTRY_OUTPUTS = 3
ENTRY_MENSAJES = "Mensaje de ejemplo"
ENTRY_BOTONES_IN = 5

ORDEN_ORIGEN = "Estación Norte"
ORDEN_DESTINO = "Estación Sur"

OUTGUI_NUM_BOTONES = 2
OUTGUI_NUM_AGVS = NUM_AGVS

SEMAFORO_X = 30.0
SEMAFORO_Y = 18.0

# Initialize Flask app and folder
app = Flask(__name__)
os.makedirs("instance", exist_ok=True)

# Base classes per DB
BaseEntryGUI = declarative_base()
BaseOrdenes = declarative_base()
BaseOutGUI = declarative_base()
BaseSemaforos = declarative_base()
BaseAGVs = declarative_base()

# DB Engines
engine_entry = create_engine("sqlite:///instance/entry_gui.db", echo=False)
engine_ordenes = create_engine("sqlite:///instance/ordenes.db", echo=False)
engine_out = create_engine("sqlite:///instance/out_gui.db", echo=False)
engine_semaforos = create_engine("sqlite:///instance/semaforos.db", echo=False)
engine_agvs = create_engine("sqlite:///instance/agvs.db", echo=False)

# Models
class DatabaseEntryGUI(BaseEntryGUI):
    __tablename__ = "database_entry_gui"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Inputs: Mapped[int] = mapped_column(Integer, nullable=False, default=ENTRY_INPUTS)
    Outputs: Mapped[int] = mapped_column(Integer, nullable=False, default=ENTRY_OUTPUTS)
    Mensajes: Mapped[str] = mapped_column(String, nullable=False, default=ENTRY_MENSAJES)
    Botones_in: Mapped[int] = mapped_column(Integer, nullable=False, default=ENTRY_BOTONES_IN)

class DatabaseOrdenes(BaseOrdenes):
    __tablename__ = "database_ordenes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    origen: Mapped[str] = mapped_column(String, nullable=False, default=ORDEN_ORIGEN)
    destino: Mapped[str] = mapped_column(String, nullable=False, default=ORDEN_DESTINO)

class DatabaseOutGUI(BaseOutGUI):
    __tablename__ = "database_out_gui"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    numero_agvs: Mapped[int] = mapped_column(Integer, nullable=False, default=OUTGUI_NUM_AGVS)
    out_botones: Mapped[int] = mapped_column(Integer, nullable=False, default=OUTGUI_NUM_BOTONES)

class DatabaseSemaforos(BaseSemaforos):
    __tablename__ = "database_semaforos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    X: Mapped[float] = mapped_column(Float, nullable=False, default=SEMAFORO_X)
    Y: Mapped[float] = mapped_column(Float, nullable=False, default=SEMAFORO_Y)

class AGV(BaseAGVs):
    __tablename__ = "agvs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, default=AGV_DEFAULT_NAME)
    x: Mapped[float] = mapped_column(Float, nullable=False, default=AGV_DEFAULT_X)
    y: Mapped[float] = mapped_column(Float, nullable=False, default=AGV_DEFAULT_Y)

# Create tables
BaseEntryGUI.metadata.create_all(engine_entry)
BaseOrdenes.metadata.create_all(engine_ordenes)
BaseOutGUI.metadata.create_all(engine_out)
BaseSemaforos.metadata.create_all(engine_semaforos)
BaseAGVs.metadata.create_all(engine_agvs)

# Insert single default rows
with Session(engine_entry) as session:
    if not session.query(DatabaseEntryGUI).first():
        session.add(DatabaseEntryGUI())
    session.commit()

with Session(engine_ordenes) as session:
    if not session.query(DatabaseOrdenes).first():
        session.add(DatabaseOrdenes())
    session.commit()

with Session(engine_out) as session:
    if not session.query(DatabaseOutGUI).first():
        session.add(DatabaseOutGUI())
    session.commit()

with Session(engine_semaforos) as session:
    if not session.query(DatabaseSemaforos).first():
        session.add(DatabaseSemaforos())
    session.commit()

# 🚀 Regenerate AGVs entirely
with Session(engine_agvs) as session:
    session.query(AGV).delete()
    for i in range(NUM_AGVS):
        session.add(AGV(name=f"{AGV_DEFAULT_NAME}-{i+1}",
                        x=AGV_DEFAULT_X,
                        y=AGV_DEFAULT_Y))
    session.commit()
