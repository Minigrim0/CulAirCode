import os
import time

import cv2
import numpy as np
from pyzbar.pyzbar import decode

from src.media import MediaModel

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.resizeWindow("frame", 1920, 1080)
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


cap = cv2.VideoCapture(2)
mediaModel = MediaModel()

startTime = time.time()
timeElapsed = 0
time_since_lost = 0
QRLost = True

blackground = np.zeros((1080, 1920, 1), dtype = "uint8")


while True:
    timeElapsed = time.time() - startTime
    startTime = time.time()
    if mediaModel.mediaLoaded():
        mediaModel.update(timeElapsed)

    ret, frame = cap.read()
    decoded = decode(frame)

    if len(decoded) > 0:
        QRLost = False
        data = decoded[0].data.decode()
        position = decoded[0].rect
        folder = f"data/{data}"

        if not mediaModel.isStillSame(folder):
            mediaModel.loadFolder(folder)
    elif mediaModel.mediaLoaded() and not QRLost:
        time_since_lost = time.time()
        QRLost = True
    elif QRLost and time.time() - time_since_lost > 1.5:
        mediaModel.kill()

    cv2.imshow("CAPT", frame)
    if not mediaModel.mediaLoaded():
        cv2.imshow('frame', blackground)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
