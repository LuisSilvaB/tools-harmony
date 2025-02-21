from flask import Blueprint, request, jsonify
from src.middlewares.validate_schema import validate_schema
from ....contants.files import PATH_TO_UPLOAD_FILES, ALLOWED_EXTENSIONS


transform_files_blueprint = Blueprint('transform_files', __name__)


@transform_files_blueprint.route('/transform-file', methods=['PUT'])
@validate_schema(None, location='json')
def transform_file():
  if 'file' is not request.files:
    return jsonify({'message': 'We cannot transform image!'}), 400
  file = request.files['file']
  print(file)
  
@transform_files_blueprint.route('/transform-files', methods=['PUT'])
def transform_files():
  return jsonify({'message': 'Hello to transform files!'})