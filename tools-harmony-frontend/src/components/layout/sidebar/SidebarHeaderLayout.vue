<script lang="ts" setup>
  import {SidebarHeader} from '@/components/ui/sidebar'
  import { useSidebar } from '@/components/ui/sidebar/utils'
  import { cn } from '@/lib/utils'
  const { open } = useSidebar()
</script>

<template>
  <SidebarHeader
    :class="cn('text-lg font-bold w-full flex flex-row justify-start items-center px-3 py-3', open ? 'justify-start': 'justify-center') ">
    <div class="flex items-center p-2 min-h-6 min-w-6 rounded-md bg-gray-500 text-white">
      <CIcon name="cilBasket" class="text-white" />
    </div>
    <span v-if="open" class="text-nowrap">
      TOOLS HARMONY
    </span>
  </SidebarHeader>
</template>
