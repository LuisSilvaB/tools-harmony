<script lang="ts" setup>
import ConvertImageTable from '@/views/dashboard/ConvertFile/components/ui/tables/ConvertFileTable.vue'
import type { DragStateType } from '../../../types/ConvertFile.type';

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
  <ConvertImageTable :dragState="props.dragState" :handleDragStart="props.handleDragStart"
    :handleDragOver="props.handleDragOver" :handleDragLeave="props.handleDragLeave" :handleDrop="props.handleDrop"
    :handleFileUpload="handleFileUpload" :onOpenInputFile="onOpenInputFile" />
</template>
