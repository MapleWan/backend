from .test import test_bp
from .auth import auth_bp
from .todo import todo_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(todo_bp, url_prefix='/api/todo')
    app.register_blueprint(test_bp, url_prefix='/api/test')