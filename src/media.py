import os
import json

from src.video import Video
from src.text import Text


class MediaModel:
    instance = None

    @staticmethod
    def getInstance():
        if MediaModel.instance is None:
            MediaModel()
        return MediaModel.instance

    def __init__(self):
        if MediaModel.instance is not None:
            raise Exception("This class is a Singleton!")
        else:
            MediaModel.instance = self
        self.media_running = False
        self.currentMedia = None
        self.folder = None

    def isStillSame(self, folder):
        return self.folder == folder

    def mediaLoaded(self):
        return self.currentMedia is not None

    def loadFolder(self, folder):
        self.kill()
        with open(os.path.join(folder, "settings.json")) as settings_file:
            settings = json.load(settings_file)

        self.folder = folder
        if settings["type"] == "video":
            self.currentMedia = Video(os.path.join(folder, settings["filename"]))
        elif settings["type"] == "text":
            self.currentMedia = Text(music=os.path.join(folder, settings["music"]), text=os.path.join(folder, settings["text"]))

    def kill(self):
        self.folder = None
        if self.currentMedia is not None:
            self.currentMedia.destroy()
        self.currentMedia = None

    def update(self, timeElapsed):
        if self.currentMedia is not None:
            if not self.currentMedia.draw(timeElapsed):
                self.kill()
        return self.currentMedia is not None
