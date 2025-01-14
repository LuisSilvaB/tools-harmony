from ..services.login_service import LoginService

login_service = LoginService()

def loginByUsernamePassword(data):
  email = data['email']
  password = data['password']
  return login_service.login(email, password)