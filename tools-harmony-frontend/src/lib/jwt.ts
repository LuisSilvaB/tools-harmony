import { useCookies } from "vue3-cookies"
import { useJwt } from '@vueuse/integrations/useJwt'
import type { JwtPayloadSubType, PermissionType } from "@/types/jwtPayloadSub.type";

const { cookies } = useCookies()

export const saveToken = (token: string) => {
  try {
    cookies.set('access_token', token, '2d', '/', '', true, 'strict');
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

export const getPermissionsByJwt = (): PermissionType[] => {
  const token = getToken();
  if (!token) {
    return [];
  }

  const { payload } = useJwt(token);
  const sub = payload.value?.sub as unknown as JwtPayloadSubType;

  if (!sub || typeof sub !== 'object' || !('permissions' in sub)) {
    return [];
  }

  const { permissions } = sub;
  return permissions;
};
