import cv2 as cv
import time

capture = cv.VideoCapture('videos/dog.mp4')

object_detector = cv.createBackgroundSubtractorMOG2()

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
    
    # Extract region of interest

    mask = object_detector.apply(frame)
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        # calc area and remove small elements
        area = cv.contourArea(cnt)
        if area > 100:
            cv.drawContours(frame, [cnt], -1, (0, 255, 0), 2)


    cv.imshow('video', frame)
    cv.imshow("mask", mask)

    time.sleep(FPS)

    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()