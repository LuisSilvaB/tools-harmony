from src import create_app
from flask import jsonify

app = create_app()

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hello World!'})

if __name__ == '__main__': 
  app.run(debug=True)