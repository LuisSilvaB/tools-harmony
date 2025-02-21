
def load_routes(app): 
  from .auth.login.login_route import login_bp
  from .auth.register.register_route import register_bp
  
  app.register_blueprint(login_bp, url_prefix='/auth')
  app.register_blueprint(register_bp, url_prefix='/auth')
  
  # Dashboard routes
  from .dashboard.transform_files.transform_files_routes import transform_files_blueprint
  
  app.register_blueprint(transform_files_blueprint, url_frefix='/dashboard')

  