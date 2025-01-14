from flask_jwt_extended import create_access_token

from .....utils.supabase import supabase

class RegisterService:
    def __init__(self):
        self.supabase = supabase
    def RegisterByEmailPassword(self, email, password, first_name, last_name, phone):
        user = self.supabase.auth.sign_up({"email": email, "password": password})
        newUser = self.supabase.table('USERS').insert({"id":user.id ,"email": email, "password": password, "first_name": first_name, "last_name": last_name, "phone": phone}).execute()
        access_token = create_access_token(identity=newUser)
        return access_token