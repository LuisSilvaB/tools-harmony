from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
from .routes.routes import load_routes
from .contants.files import PATH_TO_UPLOAD_FILES

def load_temp_folder():
    if not os.path.exists(PATH_TO_UPLOAD_FILES):
        print("Creating temp folder...")    
        os.mkdir(PATH_TO_UPLOAD_FILES)

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['PORT'] = os.getenv('PORT')
    
    JWTManager(app)
    
    CORS(app, resources={r'/*': {'origins': '*'}})
    CORS(app, resources={r'/*':{'origins':'http://localhost:8080/', 'allow_headers':'Access-Control-Allow-Origin'}})
    CORS(app, resources={r'/*':{'origins':'http://localhost:5173/', 'allow_headers':'Access-Control-Allow-Origin'}})
    
    load_routes(app)
    load_temp_folder()
    
    print("The server is running on port",  app.config['PORT'], "🚀") 
            
    return app

    
    