<script lang="ts" name="login" setup>

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { useForm } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/zod'
import { type LoginType, loginSchema } from '@/views/auth/login/shcema/login.schema'
import {
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form'
import { useMutation } from '@tanstack/vue-query'
import { loginUserByUserAndPassword } from '@/views/auth/login/services/login.service'
import { saveToken } from '@/lib/jwt'
import router from '@/router'

const formMethods = useForm<LoginType>({
  validationSchema: toTypedSchema(loginSchema),
  initialValues: {
    email: '',
    password: '',
  },
})

const mutation = useMutation({
  mutationFn: loginUserByUserAndPassword,
  onSuccess: (data) => {
    saveToken(data.data.access_token)
    router.push('/dashboard')
  },
  onError: (error) => {
    console.error('Login failed:', error)
  },
})


const onSubmit = formMethods.handleSubmit((values) => {
  mutation.mutate(values)
})

</script>

<template>
  <div class="h-full justify-center items-center flex">

    <div class="flex-1 h-full flex justify-center items-center">
      <form @submit="onSubmit" class="w-full h-full flex-col flex gap-2 justify-center items-start max-w-[400px]">
          <p class="font-bold text-xl">Login</p>
          <div class = "w-full  flex-col text-green-500 border-green-300 bg-green-100 rounded-md p-2 flex justify-start items-start h-auto text-xs">
            <p class="font-bold">User for testing</p>
            <div class="flex flex-col mt-1">
              <p class="">Username: admin</p>
              <p class="">Password: admin</p>
            </div>
          </div>
          <FormField v-slot="{ field }" name="email">
            <FormItem class="w-full">
              <FormLabel for="email">Email</FormLabel>
              <FormControl>
                <Input placeholder="Email" type="email" v-bind="field" />
              </FormControl>
              <FormDescription>Email is required</FormDescription>
              <FormMessage/>
            </FormItem>
          </FormField>
          <FormField v-slot="{ field }" name="password">
            <FormItem class="w-full">
              <FormLabel for="password">Password</FormLabel>
              <FormControl>
                <Input type="password" placeholder="*********" v-bind="field" />
              </FormControl>
              <FormDescription>Password is required</FormDescription>
              <FormMessage/>
            </FormItem>
          </FormField>
          <p>Yout don't have an account? <a href="/auth/register" class="text-blue-500 underline">Register</a></p>
          <Button> Login </Button>
      </form>
    </div>

    <div class="flex-1 h-full p-2 ">
      <div class="bg-gradient-to-r from-fuchsia-600 to-purple-600 rounded-xl w-full h-full"></div>
    </div>
  </div>
</template>
