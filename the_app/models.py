# models

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Float, String

db = SQLAlchemy()  # Single SQLAlchemy instance

# 🔹 Define models
class DatabaseEntryGUI(db.Model):
    __tablename__ = "database_entry_gui"
    __bind_key__ = "entry_gui"  # 🔹 Bind this model to database_entry_gui.db
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    AVG: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    X: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    Y: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    A: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)

class DatabaseOrdenes(db.Model):
    __tablename__ = "database_ordenes"
    __bind_key__ = "ordenes"  # 🔹 Bind this model to database_ordenes.db
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    origen: Mapped[String] = mapped_column(String, nullable=False)
    destino: Mapped[String] = mapped_column(String, nullable=False)

class DatabaseOutGUI(db.Model):
    __tablename__ = "database_out_gui"
    __bind_key__ = "out_gui"  # 🔹 Bind this model to database_out_gui.db
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    numero_agvs: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    out_botones: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

class DatabaseSemaforos(db.Model):
    __tablename__ = "database_semaforos"
    __bind_key__ = "semaforos"  # 🔹 Bind this model to database_semaforos.db
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    X: Mapped[float] = mapped_column(Float, nullable=False)
    Y: Mapped[float] = mapped_column(Float, nullable=False)
