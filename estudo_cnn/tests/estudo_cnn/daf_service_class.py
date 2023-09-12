import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

class ReadFrameOpencv:
    def __init__(self):
        self._video_file = None
        self._output_folder = None

    @property
    def video_file(self):
        return self._video_file

    @video_file.setter
    def video_file(self, path):new_frame_color = video_reader.matrix_color(frames, "RGB>GRAY")

    @property
    def output_folder(self):
        return self._output_folder

    @output_folder.setter
    def output_folder(self, path):
        self._output_folder = path

    def read_frames(self):
        if self.video_file is None:
            raise ValueError("Video file path is ncot set.")
        
        cap = cv2.VideoCapture(self.video_file)
        frames_list = []
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames_list.append(frame)

        
        cap.release()  # Importante liberar o recurso de captura após a leitura
        return frames_list

    def save_frames(self, frames):
        if self.output_folder is None:
            raise ValueError("Output folder path is not set.")
        
        os.makedirs(f"saves/{self.output_folder}", exist_ok=True)

        for i, frame in enumerate(frames):
            frame_filename = os.path.join(f"saves/{self.output_folder}", f'frame_{i:04d}.jpg')
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

    def slicing_resize_frames(self, frames, num_colunas=None, num_linhas=None, save=False, hight=None, width=None):
        if num_colunas is None:
            raise ("Value error: num_columns can't be none")
        elif num_linhas is None:
            raise ("Value error: num_linhas can't be none")
        if save:
            for i, frame in enumerate(frames):
                frame_id = f"sliced_frame_{i:04d}.jpg"
                os.makedirs(f"saves_sliced", exist_ok=True)

                partes = np.array_split(frame, num_colunas, axis=1)
                for parte in partes:
                    h_partes = np.array_split(parte, num_linhas, axis=0)
                    partes = partes + h_partes

                partes = partes[num_colunas:]
                for i, parte in enumerate(partes):
                    slice_id = f"slice_{i:03d}.jpg"
                    caminho_arquivo = f"{frame_id}/{slice_id}"
                    os.makedirs(f"saves_sliced/{caminho_arquivo}", exist_ok=True)
                    frame_filename = os.path.join(f"saves_sliced/{caminho_arquivo}", f'slice_{i:04d}.jpg')
                    cv2.imwrite(frame_filename, parte)

        elif hight!=None:
            for i, frame in enumerate(frames):
                frame = plt.figure(figsize=(hight, width))
                frame_id = f"sliced_frame_{i:04d}.jpg"
                os.makedirs(f"saves_sliced", exist_ok=True)

            partes = np.array_split(frame, num_colunas, axis=1)
            for parte in partes:
                h_partes = np.array_split(parte, num_linhas, axis=0)
                partes = partes + h_partes

            partes = partes[num_colunas:]
            for i, parte in enumerate(partes):
                slice_id = f"slice_{i:03d}.jpg"
                caminho_arquivo = f"{frame_id}/{slice_id}"
                os.makedirs(f"saves_sliced/{caminho_arquivo}", exist_ok=True)
                frame_filename = os.path.join(f"saves_sliced/{caminho_arquivo}", f'slice_{i:04d}.jpg')
                cv2.imwrite(frame_filename, parte)

        else:
            for i, frame in enumerate(frames):
                frame_id = f"sliced_frame_{i:04d}.jpg"
                os.makedirs(f"saves_sliced", exist_ok=True)

            partes = np.array_split(frame, num_colunas, axis=1)
            for parte in partes:
                h_partes = np.array_split(parte, num_linhas, axis=0)
                partes = partes + h_partes

            partes = partes[num_colunas:]
            
        return partes