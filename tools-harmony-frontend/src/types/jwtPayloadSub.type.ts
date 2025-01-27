export type JwtPayloadSubType = {
  id: string
  name: string
  email: string
  permissions: PermissionType[]
}

export type PermissionType = {
  id: string
  url?: string
  code: string
  icon?: string
  name: string
  created_at: string
  description?: string
  id_permission_main?: string
}
