import cv2 as cv
import time

capture = cv.VideoCapture('videos/kitten.mp4')

FPS = 1 / 30

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()

    if isTrue == False:
        break

    frame_resized = rescaleFrame(frame, 0.1)
    
    for i in range(0, 60):
        cv.imshow('video ' + str(i), frame_resized)

    time.sleep(FPS)

    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()