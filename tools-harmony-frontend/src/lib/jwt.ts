import { useCookies } from "vue3-cookies"

const { cookies } = useCookies()

export const saveToken = (token: string) => {
  try {
    cookies.set('access_token', token, '7d', '/', '', true, 'strict');
  } catch (error) {
    console.log(error)
  }
}

export const removeToken = () => {
  try {
    cookies.remove('access_token')
  } catch (error) {
    console.log(error)
  }
}

export const getToken = () => {
  return cookies.get('access_token')
}
