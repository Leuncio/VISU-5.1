# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer

# Create a base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# Create an instance of SQLAlchemy
db = SQLAlchemy()


class database_entry_gui(Base):
    __tablename__ = "database_entry_gui"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    AVG: Mapped[int] = mapped_column(Integer, nullable=False)
    X: Mapped[int] = mapped_column(Integer, nullable=False)
    Y: Mapped[int] = mapped_column(Integer, nullable=False)
