<script lang="ts" setup>
import { Sidebar, SidebarContent, SidebarMenuButton, SidebarMenuItem, SidebarGroup, SidebarGroupLabel, SidebarGroupContent, SidebarMenu } from '@/components/ui/sidebar'
import { SidebarHeader } from '@/components/layout/sidebar'
import { getPermissionsByJwt } from '@/lib/jwt';
import { upperLowerCase } from '@/utils/upperLowerCase.util'
import { useSidebar } from '@/components/ui/sidebar/utils'

const permissions = getPermissionsByJwt().filter(permission => !permission.id_permission_main).map((permission => (
  {...permission, description: upperLowerCase( permission.description ?? '') }
))) ?? []
const { open } = useSidebar()
</script>

<template >
    <Sidebar variant="inset" collapsible="icon" class="bg-gray-50 max-h-screen ">
      <div class="flex flex-row justify-between gap-4 p-1 items-center ">
        <SidebarHeader />
      </div>
      <SidebarContent class="flex flex-col gap-4 p-1 ">
        <SidebarGroup>
          <SidebarGroupLabel class="text-[0.7rem]">Sections</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              <SidebarMenuItem class="flex w-full items-center justify-center" v-for="(permission, index) in permissions" :key="index">
                <router-link class="flex w-full items-center justify-center" :to="`${permission.url}`">
                  <SidebarMenuButton class="hover:bg-gray-100 text-gray-600 transition-all ease-in-out w-full flex items-center justify-start" variant="default" size="sm">
                    <CIcon :icon="permission.icon ?? 'cilBasket' " :name="permission.icon ?? 'cilBasket'" class="text-gray-600 w-fit" />
                    <span v-if="open">
                      {{ permission.description }}
                    </span>
                  </SidebarMenuButton>
                </router-link>
              </SidebarMenuItem>
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>

      </SidebarContent>
    </Sidebar>
</template>
