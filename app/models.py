# __init__.py

from flask import Flask
from .views import main_bp  


def create_app():
    app = Flask(__name__)  

    # Register blueprints for modular routing
    app.register_blueprint(main_bp)

    return app