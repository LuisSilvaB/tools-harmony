
def load_routes(app): 
  from .auth.auth import auth_bp
  app.register_blueprint(auth_bp, url_prefix='/auth')

