# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, Float

# Create a base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# Create an instance of SQLAlchemy
db = SQLAlchemy()


class database_entry_gui(Base):
    __tablename__ = "database_entry_gui"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    AVG: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    X: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    Y: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    A: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
