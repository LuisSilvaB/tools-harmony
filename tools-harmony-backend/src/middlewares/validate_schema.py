from functools import wraps
from flask import request, jsonify
from marshmallow import ValidationError

def validate_schema(schema, location='json'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if location == 'json':
                data = request.json
            elif location == 'args':
                data = request.args
            elif location == 'form':
                data = request.form
            else:
                return jsonify({'message': 'Invalid location specified'}), 400

            try:
                data = schema.load(data)
            except ValidationError as err:
                return jsonify(err.messages), 400
            return f(data, *args, **kwargs)
        return decorated_function
    return decorator