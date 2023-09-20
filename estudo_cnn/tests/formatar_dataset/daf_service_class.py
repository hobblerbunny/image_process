import os
import cv2
import numpy as np
import pandas as pd

"""
mais opções de slicing, tipo uma que dividi a imagem em
1/3/1 
parametros: se o cara colocar 1 número slicing normal, se 
colocar mais de 1, outro slicing
///////////////////
opção de salvar todos os frames em uma pasta só, all_in_one
///////////////////
precisa criar um csv com as landmarks CHW(chann, height, width)
"""

class ReadFrameOpencv:
    def __init__(self):
        self._output_folder = None
        self._read_frames = None

    @property
    def output_folder(self):
        return self._output_folder

    @output_folder.setter
    def output_folder(self, path):
        self._output_folder = path

    @property
    def read_frames(self):
        if isinstance(self._read_frames, bytes):
            try:
                cap = cv2.VideoCapture(self._read_frames)
                print("cap")
            except:
                raise ValueError("Not a video")
        elif isinstance(self._read_frames, str):
            try:
                file = os.listdir(self._read_frames)
                print("file")
            except:
                raise ValueError("Not images")

        try:
            if cap:
                frames_list = []
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    frames_list.append(frame)

                cap.release()  # Importante liberar o recurso de captura após a leitura
                print("there")

        except:
            frames_list = []
            for filename in file:
                img = cv2.imread(os.path.join(self._read_frames, filename))
                frames_list.append(img)
            print("elsewhere")

        return frames_list
    
    @read_frames.setter
    def read_frames(self, frames):
        self._read_frames = frames

    def save_frames(self, frames, all_in_one=False):
        if isinstance(frames[0], np.ndarray):
            if all_in_one:
                raise ValueError("Output folder path is not set.")
            
            os.makedirs(f"{self.output_folder}", exist_ok=True)

            for i, frame in enumerate(frames):
                frame_filename = os.path.join(f"{self.output_folder}", f'frame_{i:04d}.jpg')
                cv2.imwrite(frame_filename, frame)

        elif isinstance(frames[0], np.ndarray):
            if self.output_folder is None:
                raise ValueError("Output folder path is not set.")
            
            os.makedirs(f"{self.output_folder}", exist_ok=True)

            for i, frame in enumerate(frames):
                frame_filename = os.path.join(f"{self.output_folder}", f'frame_{i:04d}.jpg')
                cv2.imwrite(frame_filename, frame)
        
        elif isinstance(frames[0], list):
            for i, tuples in enumerate(frames):
                tuple_id = f"sliced_frame_{i:04d}.jpg"
                os.makedirs(f"{self.output_folder}", exist_ok=True)

                for i, frame in enumerate(tuples):
                        slice_id = f"slice_{i:03d}.jpg"
                        caminho_arquivo = f"{tuple_id}/{slice_id}"
                        os.makedirs(f"{self.output_folder}/{caminho_arquivo}", exist_ok=True)
                        frame_filename = os.path.join(f"{self.output_folder}/{caminho_arquivo}", f'slice_{i:04d}.jpg')
                        
                        cv2.imwrite(frame_filename, frame)
        
        elif isinstance(frames[0], np.ndarray):
            if self.output_folder is None:
                raise ValueError("Output folder path is not set.")
            
            os.makedirs(f"{self.output_folder}", exist_ok=True)

            for i, frame in enumerate(frames):
                frame_filename = os.path.join(f"{self.output_folder}", f'frame_{i:04d}.jpg')
                cv2.imwrite(frame_filename, frame)

    def matrix_color(self, frames, type):
        if type=="BGR>RGB":
            change_matrix = cv2.COLOR_BGR2RGB
        elif type=="BGR>GRAY":
            change_matrix = cv2.COLOR_BGR2GRAY
        elif type=="RGB>GRAY":
            change_matrix = cv2.COLOR_RGB2GRAY

        new_frame_list = []
        for frame in frames:
            new_frame_color = cv2.cvtColor(frame, change_matrix)
            new_frame_list.append(new_frame_color)

        return new_frame_list

    def resize_frames(self, frames, height=None, width=None):
        if height is None:
            raise ("Value error: num_columns can't be none")
        elif width is None:
            raise ("Value error: num_linhas can't be none")

        if isinstance(frames[0], np.ndarray):

            result = []
            for i, frame in enumerate(frames):
                resized_image = cv2.resize(frame, (height, width))
                result.append(resized_image)

        elif isinstance(frames[0], list):

            result = []
            for i, tuples in enumerate(frames):
                partes = []

                for i, frame in enumerate(tuples):
                    resized_image = cv2.resize(frame, (height, width))
                    partes.append(resized_image)

                tuple_partes = (partes)
                result.append(tuple_partes)

        return result

    def slicing_frames(self, frames, num_linhas=None, num_colunas=None):
        if num_colunas is None:
            raise ("Value error: num_columns can't be none")
        elif num_linhas is None:
            raise ("Value error: num_linhas can't be none")

        result = []
        for i, frame in enumerate(frames):
            frame_id = f"sliced_frame_{i:04d}.jpg"
            # os.makedirs(f"saves_sliced", exist_ok=True)

            partes = np.array_split(frame, num_linhas, axis=0)
            for parte in partes:
                h_partes = np.array_split(parte, num_colunas, axis=1)
                partes = partes + h_partes

            partes = partes[num_linhas:]
            tuple_partes = (partes)
            result.append(tuple_partes)

        return result

    def landmarks(self, frames):
        for i, frame in enumerate(frames): 
            height, width, channels = self.frame.shape

        return frames
