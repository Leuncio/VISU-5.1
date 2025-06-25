from flask import Flask
from sqlalchemy import create_engine, Integer, Float, String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, Session
import os

# Configurable parameters
NUM_AGVS = 8
AGV_DEFAULT_NAME = "AGV"
AGV_DEFAULT_X = 1.0
AGV_DEFAULT_Y = 1.0

ENTRY_INPUTS = 2
ENTRY_OUTPUTS = 3
ENTRY_MENSAJES = "Mensaje de ejemplo"
ENTRY_BOTONES_IN = 5

ORDEN_ORIGEN = "Orogen A"
ORDEN_DESTINO = "Destino A"

OUTGUI_NUM_BOTONES = 2
OUTGUI_NUM_AGVS = NUM_AGVS

SEMAFORO_X = 30.0
SEMAFORO_Y = 18.0

# Initialize app and folder
app = Flask(__name__)
os.makedirs("instance", exist_ok=True)

# Base classes
BaseEntryGUI = declarative_base()
BaseOrdenes = declarative_base()
BaseOutGUI = declarative_base()
BaseSemaforos = declarative_base()
BaseAGVs = declarative_base()

# Engines
engine_entry = create_engine("sqlite:///instance/entry_gui.db", echo=False)
engine_ordenes = create_engine("sqlite:///instance/ordenes.db", echo=False)
engine_out = create_engine("sqlite:///instance/out_gui.db", echo=False)
engine_semaforos = create_engine("sqlite:///instance/semaforos.db", echo=False)
engine_agvs = create_engine("sqlite:///instance/agvs.db", echo=False)

# Models
class DatabaseEntryGUI(BaseEntryGUI):
    __tablename__ = "database_entry_gui"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Inputs: Mapped[int] = mapped_column(Integer, nullable=False)
    Outputs: Mapped[int] = mapped_column(Integer, nullable=False)
    Mensajes: Mapped[str] = mapped_column(String, nullable=False)
    Botones_in: Mapped[int] = mapped_column(Integer, nullable=False)

class DatabaseOrdenes(BaseOrdenes):
    __tablename__ = "database_ordenes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    origen: Mapped[str] = mapped_column(String, nullable=False)
    destino: Mapped[str] = mapped_column(String, nullable=False)

class DatabaseOutGUI(BaseOutGUI):
    __tablename__ = "database_out_gui"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    numero_agvs: Mapped[int] = mapped_column(Integer, nullable=False)
    out_botones: Mapped[int] = mapped_column(Integer, nullable=False)

class DatabaseSemaforos(BaseSemaforos):
    __tablename__ = "database_semaforos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    X: Mapped[float] = mapped_column(Float, nullable=False)
    Y: Mapped[float] = mapped_column(Float, nullable=False)

class AGV(BaseAGVs):
    __tablename__ = "agvs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    x: Mapped[float] = mapped_column(Float, nullable=False)
    y: Mapped[float] = mapped_column(Float, nullable=False)

# Recreate tables
BaseEntryGUI.metadata.drop_all(engine_entry)
BaseEntryGUI.metadata.create_all(engine_entry)

BaseOrdenes.metadata.drop_all(engine_ordenes)
BaseOrdenes.metadata.create_all(engine_ordenes)

BaseOutGUI.metadata.drop_all(engine_out)
BaseOutGUI.metadata.create_all(engine_out)

BaseSemaforos.metadata.drop_all(engine_semaforos)
BaseSemaforos.metadata.create_all(engine_semaforos)

BaseAGVs.metadata.drop_all(engine_agvs)
BaseAGVs.metadata.create_all(engine_agvs)

# Repopulate with fresh data
with Session(engine_entry) as session:
    session.add(DatabaseEntryGUI(
        Inputs=ENTRY_INPUTS,
        Outputs=ENTRY_OUTPUTS,
        Mensajes=ENTRY_MENSAJES,
        Botones_in=ENTRY_BOTONES_IN
    ))
    session.commit()

with Session(engine_ordenes) as session:
    session.add(DatabaseOrdenes(
        origen=ORDEN_ORIGEN,
        destino=ORDEN_DESTINO
    ))
    session.commit()

with Session(engine_out) as session:
    session.add(DatabaseOutGUI(
        numero_agvs=OUTGUI_NUM_AGVS,
        out_botones=OUTGUI_NUM_BOTONES
    ))
    session.commit()

with Session(engine_semaforos) as session:
    session.add(DatabaseSemaforos(
        X=SEMAFORO_X,
        Y=SEMAFORO_Y
    ))
    session.commit()

with Session(engine_agvs) as session:
    for i in range(NUM_AGVS):
        session.add(AGV(
            name=f"{AGV_DEFAULT_NAME}-{i+1}",
            x=AGV_DEFAULT_X,
            y=AGV_DEFAULT_Y
        ))
    session.commit()
