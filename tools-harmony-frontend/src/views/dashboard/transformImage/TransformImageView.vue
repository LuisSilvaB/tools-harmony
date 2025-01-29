<script lang="ts" setup>
import { ref, reactive } from 'vue';

const refUpload = ref<HTMLInputElement | null>(null);

const dragState = reactive({
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
    dragState.files = Array.from(files);
    console.log('Dropped files:', dragState.files);
  }
};

const handleFileUpload = (event: Event) => {
  const target = event.target as HTMLInputElement | null;
  if (target && target.files) {
    dragState.files = Array.from(target.files);
    console.log('File uploaded:', dragState.files);
  }
};

const onOpenInputFile = () => {
  refUpload.value?.click();
};

console.log("dragState.files", dragState.files);
</script>

<template>
  <div class="w-full flex-1 p-2 flex justify-center items-start border rounded-md gap-2 relative">
    <div v-if="dragState.isDragging"
      class="flex justify-center items-center flex-1 w-65 border border-dashed border-gray-300 bg-green-400 hover:cursor-pointer transition-all ease-in-out rounded-md absolute w-full h-full"
      @drop="handleDrop" @dragstart="handleDragStart" @dragover="handleDragOver" @dragleave="handleDragLeave"
      @click="onOpenInputFile" @dragover.prevent>
      <p>Drop your images here...</p>
      <input type="file" ref="refUpload" class="hidden" @change="handleFileUpload">
    </div>
    <div @drop="handleDrop" @dragstart="handleDragStart" @dragover="handleDragOver" @dragleave="handleDragLeave"
      @click="onOpenInputFile" @dragover.prevent
      class="flex justify-center items-center flex-1 w-65 h-64 border border-dashed border-gray-300 hover:border-green-500 hover:cursor-pointer transition-all ease-in-out rounded-md">
      <p>List of images</p>
    </div>
  </div>
</template>
