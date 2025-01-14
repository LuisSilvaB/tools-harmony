from flask import Blueprint, request, jsonify
from src.middlewares.validate_schema import validate_schema

from ....app.auth.login.schemas.login_schema import LoginSchemaByEmailPasswordSchema
from ....app.auth.login.controllers.login_controller import loginByUsernamePassword

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login-by-email-password', methods=['POST'])
@validate_schema(LoginSchemaByEmailPasswordSchema(), location='json')
def login(data):
    result = loginByUsernamePassword(data)
    if result['success']:
        return jsonify({"access_token": result}), 200
    return jsonify({"msg": "Invalid credentials"}), 401

