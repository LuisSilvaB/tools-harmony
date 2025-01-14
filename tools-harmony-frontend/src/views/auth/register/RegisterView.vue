<script lang="ts" name="register" setup>

import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { useForm } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/zod'
import { type RegisterType, RegisterSchema } from '@/views/auth/register/shcema/register.schema'
import {
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form'
import { SPhoneInput } from '@/components/ui/SPhoneInput'
import { useMutation } from '@tanstack/vue-query'
import { RegisterUserByUserAndPassword } from '@/views/auth/register/services/register.service'
import { saveToken } from '@/lib/jwt'
import router from '@/router'

const formMethods = useForm<RegisterType>({
  validationSchema: toTypedSchema(RegisterSchema),
  validateOnMount: false,
  keepValuesOnUnmount: true,
  initialTouched: {
    firstName: true,
    lastName: true,
    phone: true,
    email: true,
    password: true,
  },
  initialValues: {
    firstName: '',
    lastName: '',
    phone: '',
    email: '',
    password: '',
  },
})

const mutation = useMutation({
  mutationFn: RegisterUserByUserAndPassword,
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
      <form @submit="onSubmit" class="w-full h-full flex-col flex gap-2 justify-center items-start max-w-[600px]">
        <p class="font-bold text-xl">Register</p>
        <div class="flex w-full gap-2">
          <FormField v-slot="{ field }" name="firstName">
            <FormItem class="w-full">
              <FormLabel for="firstName">First Name</FormLabel>
              <FormControl>
                <Input placeholder="First Name" type="text" v-bind="field" />
              </FormControl>
              <FormDescription>First Name is required</FormDescription>
              <FormMessage />
            </FormItem>
          </FormField>
          <FormField v-slot="{ field }" name="lastName">
            <FormItem class="w-full">
              <FormLabel for="lastName">Last Name</FormLabel>
              <FormControl>
                <Input placeholder="Last Name" type="text" v-bind="field" />
              </FormControl>
              <FormDescription>Last Name is required</FormDescription>
              <FormMessage />
            </FormItem>
          </FormField>
        </div>
        <FormField v-slot="{ field }" name="phone">
            <FormItem class="w-full">
              <FormLabel for="phone">Phone</FormLabel>
              <FormControl>
                <SPhoneInput v-bind="field"  />
              </FormControl>
              <FormDescription>Phone is required</FormDescription>
              <FormMessage />
            </FormItem>
          </FormField>
        <FormField v-slot="{ field }" name="email">
          <FormItem class="w-full">
            <FormLabel for="email">Email</FormLabel>
            <FormControl>
              <Input placeholder="Email" type="email" v-bind="field" />
            </FormControl>
            <FormDescription>Email is required</FormDescription>
            <FormMessage />
          </FormItem>
        </FormField>
        <FormField v-slot="{ field }" name="password">
          <FormItem class="w-full">
            <FormLabel for="password">Password</FormLabel>
            <FormControl>
              <Input type="password" placeholder="*********" v-bind="field" />
            </FormControl>
            <FormDescription>Password is required</FormDescription>
            <FormMessage />
          </FormItem>
        </FormField>
        <p>You have an account? <a href="/auth/login" class="text-blue-500 underline">Login</a></p>
        <Button> Login </Button>
      </form>
    </div>

    <div class="flex-1 h-full p-2 ">
      <div class="bg-gradient-to-r from-fuchsia-600 to-purple-600 rounded-xl w-full h-full"></div>
    </div>
  </div>
</template>
