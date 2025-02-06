<script lang="ts" setup>
import ImageTransformHeader from '@/views/dashboard/transformImage/components/layout/transformImgaHeader/transformImgaHeader.vue';
import { ref } from 'vue';
import TransformImageTable from './components/ui/tables/transformImageTable.vue';
import { useTransformImageStore } from './store';

const refUpload = ref<HTMLInputElement | null>(null);
const { setDraggingState, setFiles, transformImageState } = useTransformImageStore();



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
    <ImageTransformHeader
      :onOpenInputFile="onOpenInputFile"
    />
    <TransformImageTable
      :dragState="transformImageState"
      :handleDragStart="handleDragStart"
      :handleDragOver="handleDragOver"
      :handleDragLeave="handleDragLeave"
      :handleDrop="handleDrop"
      :handleFileUpload="handleFileUpload"
      :onOpenInputFile="onOpenInputFile"
    />
  </div>
  <input type="file" ref="refUpload" class="hidden" @change="handleFileUpload">
</template>
