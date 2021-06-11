import time

import cv2
from ffpyplayer.player import MediaPlayer


class Video:
    def __init__(self, path):
        self.player = MediaPlayer(path)
        self.video = cv2.VideoCapture(path)
        fps = self.video.get(cv2.CAP_PROP_FPS)
        self.sleep_ms = 1 / fps
        self.grabbed = True

    def update(self):
        grabbed, frame = self.video.read()
        audio_frame, val = self.player.get_frame()
        if not grabbed:
            return False

        cv2.imshow("frame", frame)
        if val != "eof" and audio_frame is not None:
            img, t = audio_frame
        return True

    def limitFrameRate(self, timeElapsed):
        time.sleep(max(self.sleep_ms - timeElapsed, 0))

    def destroy(self):
        self.video.release()
