<script lang="ts" setup>
import ConvertImageHeader from '@/views/dashboard/ConvertFile/components/layout/ConvertFileHeader/ConvertFileHeader.vue';
import ConvertImageBody from '@/views/dashboard/ConvertFile/components/layout/ConvertFileBody/ConvertFileBody.vue';
import { ref } from 'vue';
import { useConvertImageStore } from '@/views/dashboard/ConvertFile/store';

const refUpload = ref<HTMLInputElement | null>(null);
const { setDraggingState, setFiles, ConvertImageState } = useConvertImageStore();



const handleDragStart = (event: DragEvent) => {
  event.dataTransfer?.setData('image/jpeg', 'Dragged file');
};

const handleDragOver = (event: DragEvent) => {
  event.preventDefault();
  setDraggingState(true);
};

const handleDragLeave = (event: DragEvent) => {
  event.preventDefault();
  setTimeout(() => {
    setDraggingState(false);
  }, 1000);
};

const handleDrop = (event: DragEvent) => {
  event.preventDefault();
  setDraggingState(false);
  const files = event.dataTransfer?.files;
  if (files) {
    setFiles(Array.from(files));
  }
};

const handleFileUpload = (event: Event) => {
  const target = event.target as HTMLInputElement | null;
  if (target && target.files) {
    setFiles(Array.from(target.files));
  }
};

const onOpenInputFile = () => {
  refUpload.value?.click();
};

</script>

<template>
  <div class="w-full flex-1 flex-col  p-2 flex justify-center items-start rounded-md gap-1 relative">
    <ConvertImageHeader :onOpenInputFile="onOpenInputFile" />
    <ConvertImageBody :dragState="ConvertImageState" :handleDragStart="handleDragStart" :handleDragOver="handleDragOver"
      :handleDragLeave="handleDragLeave" :handleDrop="handleDrop" :handleFileUpload="handleFileUpload"
      :onOpenInputFile="onOpenInputFile" />
  </div>
  <input type="file" ref="refUpload" class="hidden" @change="handleFileUpload">
</template>
