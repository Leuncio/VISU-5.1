# config.py

import os

# Set the URI for the database
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///database_entry_gui.db"

# Add the secret key for CSRF protection
SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'