import type { DragStateType } from '../types/transformImage.type'

export type State = {
  transformImageState: DragStateType;
}

export type Getters = {
  [key: string]: (state: State) => boolean | File[];
  getDraggingState: (state: State) => boolean;
  getFiles: (state: State) => File[];
}

export type Actions = {
  setDraggingState: ( payload: boolean) => void;
  setFiles: ( payload: File[] ) => void;
}
