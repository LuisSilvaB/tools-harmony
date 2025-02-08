import { defineStore } from 'pinia'
import type { DragStateType } from '../types/ConvertFile.type'
import type { State, Getters, Actions } from '../types/store.type'

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
    }
  }
})

export default useConvertImageStore
