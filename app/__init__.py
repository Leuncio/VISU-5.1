# __init__.py

from flask import Flask
from .views import main_bp  


def create_app():
    app = Flask(__name__)  

    # Load configuration from config.py or environment variables
    app.config.from_object('config')

    # Register blueprints for modular routing
    app.register_blueprint(main_bp)

    return app