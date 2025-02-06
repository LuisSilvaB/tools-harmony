<script lang="ts" setup>
import Button from '@/components/ui/button/Button.vue';
import { type DragStateType } from '@/views/dashboard/transformImage/types/transformImage.type';
import TransformIcon from '@radix-icons/vue/TransformIcon'
import DownloadIcon from '@radix-icons/vue/DownloadIcon'
import TrashIcon from '@radix-icons/vue/TrashIcon'

const props = defineProps<{
  dragState: DragStateType
  handleDragStart: (event: DragEvent) => void
  handleDragOver: (event: DragEvent) => void
  handleDragLeave: (event: DragEvent) => void
  handleDrop: (event: DragEvent) => void
  handleFileUpload: (event: Event) => void
  onOpenInputFile: () => void
}>()

const fromBytesToMegabytes = (bytes: number) => {
  return Math.round(bytes / 1024 / 1024 * 100) / 100;
}

const getImageUrl = (file: File) => {
  return URL.createObjectURL(file);
}

const onTransformImages = (file: File[]) => {

}

const onTransformImage = (file: File) => {
  
}

</script>

<template>
  <div class="w-full items-start flex-1 p-2 flex justify-center rounded-md gap-2 relative">
    <div v-if="props.dragState.isDragging"
      class="z-50 flex justify-center items-center flex-1 w-65  border-dashed border-gray-300 bg-green-400 hover:cursor-pointer transition-all ease-in-out rounded-md absolute w-full h-full opacity-25"
      @drop="props.handleDrop" @dragstart="props.handleDragStart" @dragover="props.handleDragOver" @dragleave="props.handleDragLeave"
      @click="props.onOpenInputFile" @dragover.prevent>
      <p>Drop your images here...</p>
    </div>
    <div @dragstart="props.handleDragStart" @dragover="props.handleDragOver" @dragover.prevent class="flex flex-1 w-full h-fit overflow-y-auto max-h-[calc(100vh-150px)]">
      <table class="w-full border-collapse rounded-lg overflow-auto">
        <thead class="bg-gray-100 text-gray-500 font-thin text-sm sticky top-0 z-10">
          <tr>
            <th class="text-center p-2"></th>
            <th class="text-center p-2">File</th>
            <th class="text-center p-2">Size</th>
            <th class="text-center p-2">Actions</th>
          </tr>
        </thead>
        <tbody class="bg-white text-gray-700 text-sm h-[20px] ">
          <tr v-for="(file) in props.dragState.files" :key="file.name" class="h-fit border-b">
            <td class="text-center p-2 h-fit flex justify-center" >
              <img :src="getImageUrl(file)" class="w-20 h-20 rounded-md object-cover border">
            </td>
            <td class="text-center p-2 text-xs">{{ file.name }}</td>
            <td class="text-center p-2">{{ fromBytesToMegabytes(file.size) }} MB</td>
            <td class="">
              <div class="flex flex-row gap-2 justify-center items-center">
                <Button size="icon" variant="default" class="flex flex-row gap-4 items-center p-2 text-white rounded" @click="props.onOpenInputFile">
                  <TransformIcon class="text-white"/>
                </Button>
                <Button size="icon" class="flex flex-row gap-4 items-center p-2 bg-blue-500 text-white rounded" @click="props.onOpenInputFile">
                  <DownloadIcon class="text-white"/>
                </Button>
                <Button size="icon" variant="destructive" class="flex flex-row gap-4 items-center p-2 rounded" @click="props.onOpenInputFile">
                  <TrashIcon class="text-white"/>
                </Button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

