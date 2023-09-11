import os
import cv2
import numpy as np

class ReadFrameOpencv:
    def __init__(self):
        self._video_file = None
        self._output_folder = None

    @property
    def video_file(self):
        return self._video_file

    @video_file.setter
    def video_file(self, path):
        self._video_file = path

    @property
    def output_folder(self):
        return self._output_folder

    @output_folder.setter
    def output_folder(self, path):
        self._output_folder = path

    def read_frames(self):
        if self.video_file is None:
            raise ValueError("Video file path is not set.")
        
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
        
        os.makedirs(self.output_folder, exist_ok=True)

        imagem = frames[0]
        # imagem = cv2.imread(frame)
        high, width, chann = imagem.shape
        print(high, width, chann)

        for i, frame in enumerate(frames):
            frame_filename = os.path.join(self.output_folder, f'frame_{i:04d}.jpg')
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

    def slicing_frames(frames):
        num_colunas = 4
        num_linhas = 4

        altura, largura, _ = frames[0].shape
        altura_parte = altura // num_linhas
        largura_parte = largura // num_colunas

        for i, frame in enumerate(frames):
            frame_id = f"sliced_frame_{i:04d}.jpg"
            frame_dir = make.os.dir(frame_id, exist_ok=True)
            partes = np.array(np.split(np.split(frame, num_colunas, axis=1), num_linhas, axis=0))

            for i, parte in enumerate(partes):
                slice_id = f"slice_{i:03d}.jpg"
                make.os.dir(f"{frame_id}/{slice_id}", exist_ok=True)
                cv2.imwrite(caminho_arquivo, parte)