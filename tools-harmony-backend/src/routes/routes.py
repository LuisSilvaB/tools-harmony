
def load_routes(app): 
  from .auth.login.login_route import login_bp
  app.register_blueprint(login_bp, url_prefix='/auth')

