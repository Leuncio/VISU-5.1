import os

# Default database (Flask-SQLAlchemy requires this)
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.getcwd(), 'instance', 'default.db')}"

# Additional bound databases
SQLALCHEMY_BINDS = {
    "entry_gui": f"sqlite:///{os.path.join(os.getcwd(), 'instance', 'database_entry_gui.db')}",
    "ordenes": f"sqlite:///{os.path.join(os.getcwd(), 'instance', 'database_ordenes.db')}",
    "out_gui": f"sqlite:///{os.path.join(os.getcwd(), 'instance', 'database_out_gui.db')}",
    "semaforos": f"sqlite:///{os.path.join(os.getcwd(), 'instance', 'database_semaforos.db')}",
}

SECRET_KEY = os.environ.get('SECRET_KEY') or "a_default_secret_key"
