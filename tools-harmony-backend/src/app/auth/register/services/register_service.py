from flask_jwt_extended import create_access_token
from .....libs.supabase import supabase

class RegisterService:
    def __init__(self):
        self.supabase = supabase

    def RegisterByEmailPassword(self, email, password, first_name, last_name, phone):
        try: 
            user = self.supabase.auth.sign_up({"email": email, "password": password})
            newUser = self.supabase.table('USERS').insert({
                "id": user.user.id,
                "email": email,
                "password": password,
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone
            }).execute().data[0]
            
            if not isinstance(newUser, dict):
                raise TypeError("Expected newUser to be a dictionary")

            identity = {
                "id": newUser["id"],
                "name": f"{newUser['first_name']} {newUser['last_name']}",
                "email": newUser["email"]
            }
            
            access_token = create_access_token(identity=identity)
            return {"success": True, "access_token": access_token}
        except Exception as e:
            return {"success": False, "msg": str(e)}