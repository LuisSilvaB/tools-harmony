
def load_routes(app): 
  from .auth.login.login_route import login_bp
  from .auth.register.register_route import register_bp
  
  app.register_blueprint(login_bp, url_prefix='/auth')
  app.register_blueprint(register_bp, url_prefix='/auth')

