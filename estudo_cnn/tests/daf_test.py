from estudo_cnn.daf_service_class import ReadFrameOpencv

video_reader = ReadFrameOpencv()
video_reader.video_file = "pelotas_teste.mp4"
video_reader.output_folder = "Saved_frames_1"

frames = video_reader.read_frames()
# new_frame_color = video_reader.matrix_color(frames=frames, type="RGB>GRAY")
video_reader.save_frames(frames)