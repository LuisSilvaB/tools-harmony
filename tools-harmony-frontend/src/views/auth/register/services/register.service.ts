import { type RegisterType } from '../shcema/register.schema'
import api from '@/lib/axios'
import { getToken } from '@/lib/jwt'

export const RegisterUserByUserAndPassword = ( data:RegisterType) => {
  return api.post('/auth/register', data)
}

