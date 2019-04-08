
from djitellopy import Tello
import cv2
import time
tello = Tello()
tello.connect()
tello.streamon()
while True:
    frame_read = tello.get_frame_read()
    frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('g', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
