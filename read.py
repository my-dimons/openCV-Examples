import cv2 as cv
import time

capture = cv.VideoCapture('videos/kitten.mp4')

FPS = 1 / 30

while True:
    isTrue, frame = capture.read()

    cv.imshow('video', frame)

    time.sleep(FPS)
    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()