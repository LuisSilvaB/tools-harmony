<script lang="ts" name="dashboard">
  import { Sidebar } from '@/components/layout/sidebar'
  import { SidebarProvider, SidebarTrigger } from '@/components/ui/sidebar'
  import { defineComponent, ref } from 'vue'
  import { useJwtParser } from '@/composables/useJwtParser'
  import { useBrowserLocation } from '@vueuse/core'
  import { upperLowerCase } from '@/utils/upperLowerCase.util'

  export default defineComponent({
  components: { Sidebar, SidebarProvider, SidebarTrigger },
  setup() {
    const { header, payload, setJwt } = useJwtParser()
    const tokenInput = ref('')

    const updateToken = () => {
      setJwt(tokenInput.value)
    }

    const pathName = upperLowerCase(useBrowserLocation().value.pathname?.split('/')[2] ?? "")

    return { header, payload, tokenInput, updateToken, pathName }
  },
})

</script>
<template>
  <div class="flex w-full h-full ">

    <SidebarProvider>
      <Sidebar />
      <div class="flex flex-col w-full h-full py-5 px-3">
        <div class = "flex w-full gap-2 items-center">
          <SidebarTrigger></SidebarTrigger>
          <span>{{pathName}}</span>
        </div>
        <router-view />
      </div>
    </SidebarProvider>

  </div>
</template>
