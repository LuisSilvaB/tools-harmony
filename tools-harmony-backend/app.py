from flask import Flask, jsonify
from products import products

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/products', methods=['GET'])
def ping():
  return jsonify({"products": products})

@app.route('/products/<int:id>', methods=['GET'])
def getProduct(id):
  productFound = next((product for product in products if product['id'] == id), None)
  return jsonify({"product": productFound})
  # productFound = [ product from product in products if product['id'] == id ]

if __name__ == '__main__':
  app.run(debug=True, port=5000)
  
