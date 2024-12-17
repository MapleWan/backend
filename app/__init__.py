from flask import Flask
from config import Config
from app.extensions import db, login_manager
from app.routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    register_blueprints(app)

    return app