import { defineStore } from 'pinia'
import type { DragStateType } from '../types/ConvertFile.type'
import type { State, Getters, Actions } from '../types/store.type'
import api from '@/lib/axios'
import { getToken } from '@/lib/jwt'

export const useConvertImageStore = defineStore<'ConvertImage', State, Getters, Actions>('ConvertImage', {
  state: (): State => (
    {
      ConvertImageState: {
        isDragging: false,
        files: [] as File[]
      } as DragStateType
    }
  ),
  getters: {
    getDraggingState: (state) => state.ConvertImageState.isDragging,
    getFiles: (state) => state.ConvertImageState.files
  },
  actions: {
    setDraggingState(isDragging: boolean) {
      this.ConvertImageState.isDragging = isDragging;
    },
    setFiles(file: File[]) {
      this.ConvertImageState.files = [...this.ConvertImageState.files, ...file];
    },

    // Async functions

    async convertFile(file: File) {
      try {
        const formData = new FormData();
        formData.append('file', file);
        const response = await api.put('/dashboard/transform-file')
        console.log(response)
      } catch (error) {
        console.log(error)
      }
    }
  }
})

export default useConvertImageStore
