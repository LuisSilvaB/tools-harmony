from .....libs.supabase import supabase

class PermissionService:
    def __init__(self):
        self.supabase = supabase
        
    def findPermissionsByUserId(self, user_id): 
        try:
            response = self.supabase.from_('USER_ROL').select('*, ROL_PERMISSION(*, PERMISSIONS(*))').eq('USER_ID', user_id).execute()
            user_rol = response.data[0]
            
            # Verificar que rol_permissions_data es una lista
            if not isinstance(user_rol, dict):
                raise TypeError("Expected rol_permissions_data to be a dictionary")

            permissions = []
            
            print(response)
            
            rol_permission_details = user_rol.get('ROL_PERMISSION', [])
            for permission in rol_permission_details:
              permission_details = permission.get('PERMISSIONS', {})
              if permission_details:
                permissions.append(permission_details)
            
            print("Permissions", permissions)
            
            return {"success": True, "permissions": permissions}
        except Exception as e:
            return {"success": False, "msg": str(e)}
    
    def createUserRole(self, user_id, rol_id):
        try:
            response = self.supabase.table('USER_ROL').insert({
                "USER_ID": user_id,
                "ROL_ID": rol_id
            }).execute().data[0]
            
            if not isinstance(response, dict):
                raise TypeError("Expected response to be a dictionary")
            
            return {"success": True, "msg": response}
        except Exception as e:  
            return {"success": False, "msg": str(e)}