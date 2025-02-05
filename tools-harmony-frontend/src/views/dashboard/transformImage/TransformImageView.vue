<script lang="ts" setup>
import ImageTransformHeader from '@/views/dashboard/transformImage/components/layout/transformImgaHeader/transformImgaHeader.vue';
import { type DragStateType } from './types/transformImage.type';
import { ref, reactive } from 'vue';
import TransformImageTable from './components/ui/tables/transformImageTable.vue';


const refUpload = ref<HTMLInputElement | null>(null);

const dragState = reactive<DragStateType>({
  isDragging: false,
  files: [] as File[],
});

const handleDragStart = (event: DragEvent) => {
  event.dataTransfer?.setData('image/jpeg', 'Dragged file');
};

const handleDragOver = (event: DragEvent) => {
  event.preventDefault();
  dragState.isDragging = true;
  console.log('Dragged over:', event.dataTransfer?.files);
};

const handleDragLeave = (event: DragEvent) => {
  event.preventDefault();
  setTimeout(() => {
    dragState.isDragging = false;
  }, 2000);
};

const handleDrop = (event: DragEvent) => {
  event.preventDefault();
  dragState.isDragging = false;
  const files = event.dataTransfer?.files;
  if (files) {
    dragState.files = [...dragState.files, ...Array.from(files)];
    console.log('Dropped files:', dragState.files);
  }
};

const handleFileUpload = (event: Event) => {
  const target = event.target as HTMLInputElement | null;
  if (target && target.files) {
    dragState.files = [...dragState.files, ...Array.from(target.files)];
    console.log('File uploaded:', dragState.files);
  }
};

const onOpenInputFile = () => {
  refUpload.value?.click();
};

console.log("dragState.files", dragState.files);
</script>

<template>
  <div class="w-full flex-1 flex-col  p-2 flex justify-center items-start rounded-md gap-1 relative">
    <ImageTransformHeader
      :onOpenInputFile="onOpenInputFile"
    />
    <TransformImageTable
      :dragState="dragState"
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
