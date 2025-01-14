from flask_jwt_extended import create_access_token

from ...utils.supabase import supabase

class LoginService:
    def __init__(self):
        self.supabase = supabase
    def login(self, email, password):
        user = self.supabase.auth.sign_in_with_password({"email": email, "password": password})
        access_token = create_access_token(identity=user)
        return access_token