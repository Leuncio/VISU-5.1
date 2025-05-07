# config.py

import os

# Add the secret key for CSRF protection
SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'