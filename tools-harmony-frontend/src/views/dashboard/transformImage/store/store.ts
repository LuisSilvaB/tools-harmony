import { defineStore } from 'pinia'
import type { DragStateType } from '../types/transformImage.type'
import type { State, Getters, Actions } from '../types/store.type'

export const useTransformImageStore = defineStore<'transformImage', State, Getters, Actions>('transformImage', {
  state: (): State => (
    {
      transformImageState: {
        isDragging: false,
        files: [] as File[]
      } as DragStateType
    }
  ),
  getters: {
    getDraggingState: (state) => state.transformImageState.isDragging,
    getFiles: (state) => state.transformImageState.files
  },
  actions: {
    setDraggingState(isDragging: boolean) {
      this.transformImageState.isDragging = isDragging;
    },
    setFiles(file: File[]) {
      this.transformImageState.files = [...this.transformImageState.files, ...file];
    }
  }
})
