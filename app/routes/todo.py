from flask import Blueprint, jsonify, request, abort
from flask_login import login_required, current_user
from app.models.todo import Todo
from app.services.todo_service import add_todo, get_todos, update_todo, delete_todo

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/', methods=['GET', 'POST'])
@login_required
def todos():
    # Implement Todo list and creation logic here using services
    pass

@todo_bp.route('/<int:id>', methods=['PUT', 'DELETE'])
@login_required
def todo(id):
    # Implement Todo update and deletion logic here using services
    pass