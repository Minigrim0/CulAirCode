from pydub import AudioSegment
from pydub.playback import play
import cv2
import simpleaudio


class Text:
    def __init__(self, music, text):
        self.music = AudioSegment.from_mp3(music)
        self.duration = self.music.duration_seconds
        self.music = simpleaudio.play_buffer(
            self.music.raw_data,
            num_channels= self.music.channels,
            bytes_per_sample= self.music.sample_width,
            sample_rate= self.music.frame_rate
        )
        self.text = cv2.imread(text)
        self.time = 0

    def draw(self, timeElapsed):
        self.time += timeElapsed
        cv2.imshow("frame", self.text)
        return self.time < self.duration

    def destroy(self):
        self.music.stop()
