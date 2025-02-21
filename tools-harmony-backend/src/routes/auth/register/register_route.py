from flask import Blueprint, request, jsonify
from src.middlewares.validate_schema import validate_schema

from ....app.auth.register.schemas.register_schema import RegisterSchemaByEmailPasswordSchema
from ....app.auth.register.controllers.register_controller import registerByUsernamePassword

from ....utils.get_error_messages import get_error_message

register_bp = Blueprint('register_bp', __name__)

@register_bp.route('/register-by-email-password', methods=['POST'])
@validate_schema(RegisterSchemaByEmailPasswordSchema(), location='json')
def login(data):
    try: 
        result = registerByUsernamePassword(data)
        if result['success']:
            return jsonify({"data": result}), 200
        else:
            return jsonify({"error": result['msg'] }), 400
    except Exception as e:
        error_message = get_error_message(e)
        return jsonify({"error": error_message }), 400
