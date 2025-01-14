import { z } from 'zod'

export const RegisterSchema = z.object({
  firstName: z.string().min(3, 'First name is too short, min 3 characteres').max(20, 'First name is too long, max 20 characteres'),
  lastName: z.string().min(3, 'Last name is too short, min 3 characteres').max(20, 'Last name is too long, max 20 characteres'),
  phone: z.string().min(9, 'Phone is too short, min 9 characteres').max(20, 'Phone is too long, max 20 characteres'),
  email: z.string().email(),
  password: z
    .string()
    .min(3, 'Password is too short, max 3 characteres')
    .max(20, 'Password is too long, max 20 characteres'),
})

export type RegisterType = z.infer<typeof RegisterSchema>
