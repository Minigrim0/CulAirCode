import os
import time

import cv2
from pyzbar.pyzbar import decode

from src.media import MediaModel

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.resizeWindow("frame", 1920, 1080)
cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


cap = cv2.VideoCapture(0)
mediaModel = MediaModel()

startTime = time.time()
timeElapsed = 0

while True:
    startTime = time.time()
    ret, frame = cap.read()

    if not mediaModel.update():

        decoded = decode(frame)
        if len(decoded) > 0:
            data = decoded[0].data.decode()
            position = decoded[0].rect

            if data == "4":
                mediaModel.loadFolder("data/4")

        cv2.imshow("frame", frame)
    cv2.waitKey(10)

    timeElapsed = time.time() - startTime
    mediaModel.limitFrameRate(timeElapsed)

cap.release()
cv2.destroyAllWindows()
