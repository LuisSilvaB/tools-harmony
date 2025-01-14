import { z } from 'zod'

export const loginSchema = z.object({
  email: z
    .string()
    .min(3, 'Username is too short, max 3 characteres')
    .max(20, 'Username is too long, max 20 characteres'),
  password: z
    .string()
    .min(3, 'Password is too short, max 3 characteres')
    .max(20, 'Password is too long, max 20 characteres'),
})

export type LoginType = z.infer<typeof loginSchema>
