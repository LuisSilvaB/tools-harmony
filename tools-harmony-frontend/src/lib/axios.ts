// axios.ts
import axios from 'axios'
import { useCookies } from 'vue3-cookies'
import router from '@/router'

const { cookies } = useCookies()
const excludeRoutes = ['/auth/login', '/auth/register']

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Requested-With',
  },
})

const setupInterceptors = () => {
  const currentRoute = router.currentRoute.value.path

  if (!excludeRoutes.includes(currentRoute)) {
    api.interceptors.request.use((config) => {
      const token = cookies.get('access_token')
      if (token) {
        config.headers.Authorization = `Bearer ${token}`
      }
      return config
    },
      (error) => {
        if (error.response.status === 401) {
          router.push('/auth/login')
        }
        return Promise.reject(error)
      }
    )
  }
}

export default api
export { setupInterceptors }
