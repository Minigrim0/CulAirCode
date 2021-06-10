import cv2
from pyzbar.pyzbar import decode


# Video source - can be camera index number given by 'ls /dev/video*
# or can be a video file, e.g. '~/Video.avi'
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    print(decode(frame))

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow("frame", gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# import cv2
#
# camera = cv2.VideoCapture(0)
# for i in range(10):
#     return_value, image = camera.read()
#     cv2.imwrite('opencv'+str(i)+'.png', image)
# del(camera)
