import os

from flask_jwt_extended import create_access_token
from flask import jsonify

from .....libs.supabase import supabase
from ...permissions.services.permission_service import PermissionService

permissionService = PermissionService()

class RegisterService:
    def __init__(self):
        self.supabase = supabase
        self.permissionService = permissionService
        self.permission_admin_rol_id = os.environ.get("ADMIN_ROL_ID")

    def RegisterByEmailPassword(self, email, password, first_name, last_name, phone):
        try: 
            if not self.permission_admin_rol_id or not isinstance(self.permission_admin_rol_id, str):
                raise TypeError("Expected permission_admin_rol_id to be a string")
            
            user = self.supabase.auth.sign_up({"email": email, "password": password})
            newUser = self.supabase.table('USERS').insert({
                "id": user.user.id,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone
            }).execute().data[0]
            
            # Create user role
            self.permissionService.createUserRole(user.user.id, self.permission_admin_rol_id)
            
            if not isinstance(newUser, dict):
                raise TypeError("Expected newUser to be a dictionary")
        
            # Get permissions 
            permissions_data = self.permissionService.findPermissionsByUserId(user.user.id)
            
            print(permissions_data)
            
            if not isinstance(permissions_data, list):
                raise TypeError("Expected permissions to be a list") 
            
            identity = {
                "id": newUser["id"],
                "name": f"{newUser['first_name']} {newUser['last_name']}",
                "email": newUser["email"],
                "permissions": jsonify(permissions_data)
            }
            
            access_token = create_access_token(identity=identity)
            return {"success": True, "access_token": access_token}
        except Exception as e:
            return {"success": False, "msg": str(e)}