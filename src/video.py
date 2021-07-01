import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
from moviepy.editor import VideoFileClip


class Video:
    def __init__(self, path, queueSize=1024):
        self.stream = VideoFileClip(path).rotate(90)
        self.path = path
        cv2.setWindowProperty(
            "frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        self.sleep_ms = 1 / self.stream.fps
        self.current_frame = 0
        self.time = 0

        self.player = MediaPlayer(self.path)

        self.back = np.zeros((1080, 1920, 3), np.uint8)
        self.back[:, :] = (0, 0, 0)

    def draw(self, timeElapsed):
        self.time += timeElapsed
        frame = cv2.resize(self.stream.get_frame(self.time), (608, 1080))
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        height, width = frame.shape[:2]
        new_image = self.back
        x_offset = 656
        new_image[:, x_offset:x_offset + width] = frame

        cv2.imshow("frame", new_image)

        audio_frame, val = self.player.get_frame()
        if val != "eof" and audio_frame is not None:
            img, t = audio_frame
        return self.time < self.stream.duration

    def destroy(self):
        pass
