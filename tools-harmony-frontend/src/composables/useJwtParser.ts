import { ref } from 'vue'
import { useJwt } from '@vueuse/integrations/useJwt'
import { useCookies } from 'vue3-cookies'

export function useJwtParser(initialToken = '') {
  const { cookies } = useCookies()
  const encodedJwt = ref(cookies.get('access_token') || initialToken)
  const { header, payload } = useJwt(encodedJwt)

  const setJwt = (newToken:string) => {
    encodedJwt.value = newToken
  }

  return { encodedJwt, header, payload, setJwt }
}
