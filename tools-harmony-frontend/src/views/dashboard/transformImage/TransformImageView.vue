<script lang="ts" setup>
import ImageTransformHeader from '@/views/dashboard/transformImage/components/layout/transformImgaHeader/transformImgaHeader.vue';
import type Button from '@/components/ui/button/Button.vue';
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
    dragState.files = [...dragState.files, ...Array.from(files)];
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

const getImageUrl = (file: File) => {
  return URL.createObjectURL(file);
}

const fromBytesToMegabytes = (bytes: number) => {
  return Math.round(bytes / 1024 / 1024 * 100) / 100;
}
console.log("dragState.files", dragState.files);
</script>

<template>
  <div class="w-full flex-1 flex-col  p-2 flex justify-center items-start rounded-md gap-1 relative">
    <ImageTransformHeader />

    <div v-if="dragState.isDragging"
      class="z-50 flex justify-center items-center flex-1 w-65 border border-dashed border-gray-300 bg-green-400 hover:cursor-pointer transition-all ease-in-out rounded-md absolute w-full h-full"
      @drop="handleDrop" @dragstart="handleDragStart" @dragover="handleDragOver" @dragleave="handleDragLeave"
      @click="onOpenInputFile" @dragover.prevent>
      <p>Drop your images here...</p>
    </div>
    <div v-else class="hidden"></div>
    <div v-if="!dragState.isDragging"  @dragstart="handleDragStart" @dragover="handleDragOver" @click="onOpenInputFile" @dragover.prevent class="flex flex-1 w-full h-full cursor-pointer">
      <table class="w-full h-fit border-collapse rounded-t-lg overflow-auto">
        <thead class="bg-gray-100 text-gray-500 font-thin text-sm rounded-t-lg border-collapse">
          <tr>
            <th class="text-center p-2">ID</th>
            <th class="text-center p-2">File</th>
            <th class="text-center p-2">Size</th>
            <th class="text-center p-2">actions</th>
          </tr>
        </thead>
      </table>
    </div>

    <input type="file" ref="refUpload" class="hidden" @change="handleFileUpload">
  </div>
</template>
