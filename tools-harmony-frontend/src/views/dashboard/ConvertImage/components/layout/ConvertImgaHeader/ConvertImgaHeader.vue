<script lang="ts" setup>
  import Button from '@/components/ui/button/Button.vue'
import UploadIcon from '@radix-icons/vue/UploadIcon'
  const props = defineProps<{
    onOpenInputFile: () => void
  }>()
</script>
<template>
  <div class="w-full justify-end flex p-2 text-xs">
    <Button size="icon" class="flex flex-row gap-4 items-center p-2 bg-blue-500 text-white rounded" @click="props.onOpenInputFile">
      <UploadIcon class="text-white"/>
    </Button>
  </div>
</template>

