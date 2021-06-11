import os
import json

from src.video import Video


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

    def loadFolder(self, folder):
        with open(os.path.join(folder, "settings.json")) as settings_file:
            settings = json.load(settings_file)

        if settings["type"] == "video":
            self.currentMedia = Video(os.path.join(folder, settings["filename"]))

    def update(self):
        if self.currentMedia is not None:
            if not self.currentMedia.update():
                self.currentMedia.destroy()
                self.currentMedia = None
        return self.currentMedia is not None

    def limitFrameRate(self, timeElapsed):
        if self.currentMedia is not None:
            self.currentMedia.limitFrameRate(timeElapsed)
        return self.currentMedia is not None
