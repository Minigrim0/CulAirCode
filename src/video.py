import time

import cv2
from ffpyplayer.player import MediaPlayer
from moviepy.editor import VideoFileClip


class Video:
    def __init__(self, path, queueSize=1024):
        self.stream = VideoFileClip(path).rotate(90)
        cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        self.player = MediaPlayer(path)
        self.sleep_ms = 1 / self.stream.fps
        self.current_frame = 0
        self.time = 0

    def draw(self, timeElapsed):
        self.time += timeElapsed
        frame = self.stream.get_frame(self.time)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.imshow("frame", frame)

        audio_frame, val = self.player.get_frame()
        if val != "eof" and audio_frame is not None:
            img, t = audio_frame
        return self.time < self.stream.duration

    def destroy(self):
        pass
