from ..services.register_service import RegisterService

register_service = RegisterService()

def registerByUsernamePassword(data):
  email = data['email']
  password = data['password']
  first_name = data['firstName']
  last_name = data['lastName']
  phone = data['phone']
  return register_service.RegisterByEmailPassword(email, password, first_name, last_name, phone)
  