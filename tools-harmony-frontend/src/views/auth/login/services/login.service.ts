import { type LoginType } from '../shcema/login.schema'
import api from '@/lib/axios'
import { getToken } from '@/lib/jwt'

export const loginUserByUserAndPassword = ( credentials:LoginType ) => {
  return api.post('/auth/login', credentials)
}

export const isAuthenticated = () => {
  const token = getToken()
  return !!token
}
