<script lang="ts" setup>
  import {SidebarProvider, SidebarTrigger, Sidebar, SidebarContent, SidebarMenuButton,SidebarMenuItem, SidebarGroup, SidebarGroupLabel, SidebarGroupContent, SidebarMenu } from '@/components/ui/sidebar'
  import { SidebarHeader } from '@/components/layout/sidebar'

</script>

<template >
  <SidebarProvider>
    <Sidebar variant="inset" collapsible="icon" class="bg-gray-50 max-h-screen">
      <div class="flex flex-row justify-between gap-4 p-1 items-center ">
        <SidebarHeader />
        <SidebarTrigger></SidebarTrigger>
      </div>
      <SidebarContent class="flex flex-col gap-4 p-1 ">
        <SidebarGroup>
          <SidebarGroupLabel class="text-[0.7rem]">Sections</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              <SidebarMenuItem>
                <SidebarMenuButton class="hover:bg-gray-100 transition-all ease-in-out" variant="default" size="sm">
                  TEST
                </SidebarMenuButton>
              </SidebarMenuItem>
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>

      </SidebarContent>
    </Sidebar>
  </SidebarProvider>
</template>
