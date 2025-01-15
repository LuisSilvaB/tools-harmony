import { type RegisterType } from '../shcema/register.schema'
import api from '@/lib/axios'

export const RegisterUserByUserAndPassword = ( data:RegisterType) => {
  return api.post('/auth/register-by-email-password', data)
}

