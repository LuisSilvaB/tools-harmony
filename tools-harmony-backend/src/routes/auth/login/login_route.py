from flask import Blueprint, request, jsonify
from src.middlewares.validate_schema import validate_schema

from ....app.auth.login.schemas.login_schema import LoginSchemaByEmailPasswordSchema
from ....app.auth.login.controllers.login_controller import loginByUsernamePassword

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login-by-email-password', methods=['POST'])
@validate_schema(LoginSchemaByEmailPasswordSchema(), location='json')
def login(data):
    try:
        result = loginByUsernamePassword(data)
        if result['success']:
            return jsonify({"data": result}), 200
        else: 
            return jsonify({"error": result['msg']}), 400
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 401
