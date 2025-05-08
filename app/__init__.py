# __init__.py

from flask import Flask
from .views import main_bp  
from .py_to_js import js_bp  # Import the JavaScript blueprint


def create_app():
    app = Flask(__name__)  

    # Load configuration from config.py or environment variables
    app.config.from_object('config')

    # Register blueprints for modular routing
    
    app.register_blueprint(main_bp) # Register the main blueprint

    app.register_blueprint(js_bp, url_prefix='/api')

    return app