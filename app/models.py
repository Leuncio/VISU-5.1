# models

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, Float, String
from config import SQLALCHEMY_DATABASES
from sqlalchemy import create_engine

# Create a base for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# 🔹 Create separate database connections using `config.py`
db_entry = create_engine(SQLALCHEMY_DATABASES["entry_gui"])
db_ordenes = create_engine(SQLALCHEMY_DATABASES["ordenes"])
db_out_gui = create_engine(SQLALCHEMY_DATABASES["out_gui"])
db_semaforos = create_engine(SQLALCHEMY_DATABASES["semaforos"])

# 🔹 Define models
class DatabaseEntryGUI(Base):
    __tablename__ = "database_entry_gui"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    AVG: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    X: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    Y: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    A: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)

class DatabaseOrdenes(Base):
    __tablename__ = "database_ordenes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    origen: Mapped[String] = mapped_column(String, nullable=False)
    destino: Mapped[String] = mapped_column(String, nullable=False)

class DatabaseOutGUI(Base):
    __tablename__ = "database_out_gui"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    numero_agvs: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    out_botones: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

class DatabaseSemaforos(Base):
    __tablename__ = "database_semaforos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    X: Mapped[float] = mapped_column(Float, nullable=False)
    Y: Mapped[float] = mapped_column(Float, nullable=False)

# 🔹 Create tables in their respective databases
Base.metadata.create_all(db_entry)
Base.metadata.create_all(db_ordenes)
Base.metadata.create_all(db_out_gui)
Base.metadata.create_all(db_semaforos)
