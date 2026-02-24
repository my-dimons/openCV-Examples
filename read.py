import numpy as np
import cv2 as cv
import time

cam = cv.VideoCapture(0)

frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

prev_frame_time = 0
new_frame_time = 0

# FPS Text Consts
FPS_TEXT_COLOR = (255, 255, 255)
FPS_TEXT_POS = (2, 15)

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def calculateFPS():
    global prev_frame_time
    new_frame_time = time.time()

    fps = "FPS: " + str(int(1 / (new_frame_time - prev_frame_time)))
    prev_frame_time = new_frame_time

    return fps

def putFpsText(frame, fps, position):

    font = cv.QT_FONT_NORMAL

    cv.putText(frame, fps, position, font, 0.5, FPS_TEXT_COLOR, 1, cv.LINE_AA)

def read_camera():
    while True:
        ret, frame = cam.read() 

        if ret == False:
            break

        fps = calculateFPS()

        putFpsText(frame, fps, FPS_TEXT_POS)

        resized_frame = rescaleFrame(frame, 1.5)

        cv.imshow('webcam', resized_frame)  

        if cv.waitKey(1) == ord('q'):
            break

read_camera()
cam.release()
cv.destroyAllWindows()
