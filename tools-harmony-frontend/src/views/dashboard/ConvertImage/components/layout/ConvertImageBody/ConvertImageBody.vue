<script lang="ts" setup>
  import ConvertImageTable from '@/views/dashboard/ConvertImage/components/ui/tables/ConvertImageTable.vue'
  import type { DragStateType } from '../../../types/ConvertImage.type';

  const props = defineProps<{
  dragState: DragStateType
  handleDragStart: (event: DragEvent) => void
  handleDragOver: (event: DragEvent) => void
  handleDragLeave: (event: DragEvent) => void
  handleDrop: (event: DragEvent) => void
  handleFileUpload: (event: Event) => void
  onOpenInputFile: () => void
}>()

</script>
<template>
    <ConvertImageTable
      :dragState="props.dragState"
      :handleDragStart="props.handleDragStart"
      :handleDragOver="props.handleDragOver"
      :handleDragLeave="props.handleDragLeave"
      :handleDrop="props.handleDrop"
      :handleFileUpload="handleFileUpload"
      :onOpenInputFile="onOpenInputFile"
    />
</template>

