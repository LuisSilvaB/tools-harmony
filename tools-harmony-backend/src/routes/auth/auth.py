from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from src.middlewares.validate_schema import validate_schema

from ...app.auth.login.login_schema import LoginSchema

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
@validate_schema(LoginSchema(), location='json')
def login(data):
    username = data['username']
    password = data['password']
    
    if username != "test" or password != "test":
        return jsonify({'message': 'Invalid credentials'}), 401
    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200
