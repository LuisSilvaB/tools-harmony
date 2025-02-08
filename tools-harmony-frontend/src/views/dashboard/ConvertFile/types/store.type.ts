import type { DragStateType } from './ConvertFile.type'

export type State = {
  ConvertImageState: DragStateType;
}

export type Getters = {
  [key: string]: (state: State) => boolean | File[];
  getDraggingState: (state: State) => boolean;
  getFiles: (state: State) => File[];
}

export type Actions = {
  setDraggingState: (payload: boolean) => void;
  setFiles: (payload: File[]) => void;
}
