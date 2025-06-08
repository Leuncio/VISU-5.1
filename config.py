# config.py

import os

# Define multiple SQLite databases
SQLALCHEMY_DATABASES = {
    "entry_gui": f"sqlite:///{os.path.join(os.getcwd(), 'instance', 'database_entry_gui.db')}",
    "ordenes": f"sqlite:///{os.path.join(os.getcwd(), 'instance', 'database_ordenes.db')}",
    "out_gui": f"sqlite:///{os.path.join(os.getcwd(), 'instance', 'database_out_gui.db')}",
    "semaforos": f"sqlite:///{os.path.join(os.getcwd(), 'instance', 'database_semaforos.db')}",
}

# Secret key for Flask security (unrelated to DB but needed)
SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
