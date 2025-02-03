<script lang="ts" setup>
  import Button from '@/components/ui/button/Button.vue'
  import { PlusIcon } from '@radix-icons/vue'
</script>
<template>
  <div class="w-full justify-end flex p-2 text-xs">
    <Button class="flex flex-row gap-4 items-center" size="icon" variant="default">
      <PlusIcon class="text-white"/>
    </Button>
  </div>
</template>

