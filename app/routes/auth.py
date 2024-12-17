from flask import Blueprint, jsonify, request, abort
from werkzeug.security import generate_password_hash
from app.models.user import User
from app.services.auth_service import load_user, register_user, authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    # Implement registration logic here using register_user service
    pass

@auth_bp.route('/login', methods=['POST'])
def login():
    # Implement login logic here using authenticate_user service
    pass

# Add logout route if necessary