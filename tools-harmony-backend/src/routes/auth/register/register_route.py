from flask import Blueprint, request, jsonify
from src.middlewares.validate_schema import validate_schema

from ....app.auth.register.schemas.register_schema import RegisterSchemaByEmailPasswordSchema
from ....app.auth.register.controllers.register_controller import registerByUsernamePassword

register_bp = Blueprint('register_bp', __name__)

@register_bp.route('/register-by-email-password', methods=['POST'])
@validate_schema(RegisterSchemaByEmailPasswordSchema(), location='json')
def login(data):
    result = registerByUsernamePassword(data)
    if result['success']:
        return jsonify({"access_token": result}), 200
    return jsonify({"msg": "Invalid credentials"}), 401

