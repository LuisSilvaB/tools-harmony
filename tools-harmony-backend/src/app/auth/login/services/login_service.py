from flask_jwt_extended import create_access_token

from .....libs.supabase import supabase

class LoginService:
    def __init__(self):
        self.supabase = supabase
    def login_by_email_password(self, email, password):
        try:             
            userSign = self.supabase.auth.sign_in_with_password({"email": email, "password": password})
            if not userSign:
                raise ValueError("Invalid email or password")
            userData = self.supabase.from_('USERS').select('id, first_name, last_name, email').eq('email', email).execute().data[0]
            if not isinstance(userData, dict):
                raise TypeError("Expected userData to be a dictionary")
            identity = {
                "id": userData['id'],
                "name": f"{userData['first_name']} {userData['last_name']}",
                "email": userData['email']
            }
            access_token = create_access_token(identity=identity)
            return {"success": True, "access_token": access_token}
        except Exception as e:
            return {"success": False, "msg": str(e)}