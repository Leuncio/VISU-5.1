from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, Float, String

# Crear una base para los modelos
class Base(DeclarativeBase):
    pass

# Instancia de la base de datos
db = SQLAlchemy()

# 🔹 Tabla para entrada de datos GUI
class DatabaseEntryGUI(Base):
    __tablename__ = "database_entry_gui"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    AVG: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    X: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    Y: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    A: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)

# 🔹 Tabla para órdenes (origen, destino)
class DatabaseOrdenes(Base):
    __tablename__ = "database_ordenes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    origen: Mapped[String] = mapped_column(String, nullable=False)
    destino: Mapped[String] = mapped_column(String, nullable=False)

# 🔹 Tabla para salida de GUI (AGVs y botones)
class DatabaseOutGUI(Base):
    __tablename__ = "database_out_gui"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    numero_agvs: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    out_botones: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

# 🔹 Tabla para semáforos (coordenadas)
class DatabaseSemaforos(Base):
    __tablename__ = "database_semaforos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    X: Mapped[float] = mapped_column(Float, nullable=False)
    Y: Mapped[float] = mapped_column(Float, nullable=False)
