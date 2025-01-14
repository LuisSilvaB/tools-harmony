from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
from .routes.routes import load_routes

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    JWTManager(app)
    
    CORS(app, resources={r'/*': {'origins': '*'}})
    CORS(app, resources={r'/*':{'origins':'http://localhost:8080/', 'allow_headers':'Access-Control-Allow-Origin'}})
    CORS(app, resources={r'/*':{'origins':'http://localhost:5173/', 'allow_headers':'Access-Control-Allow-Origin'}})
    
    load_routes(app)
    
    return app

    
    