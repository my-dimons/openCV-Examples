import numpy as np
import cv2 as cv
import time

cam = cv.VideoCapture(0);

frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

prev_frame_time = 0;
new_frame_time = 0;

# FPS Text Consts
FPS_TEXT_COLOR = (255, 255, 255)
FPS_TEXT_POS = (2, 15)

def putFpsText(frame):
    global prev_frame_time

    font = cv.FONT_HERSHEY_SIMPLEX
    new_frame_time = time.time()

    fps = "FPS: " + str(int(1 / (new_frame_time - prev_frame_time)))
    prev_frame_time = new_frame_time

    cv.putText(frame, fps, FPS_TEXT_POS, font, 0.5, FPS_TEXT_COLOR, 1, cv.LINE_AA)

def read_camera():
    while True:
        ret, frame = cam.read();    

        putFpsText(frame)

        cv.imshow('webcam', frame)  

        if cv.waitKey(1) == ord('q'):
            break

read_camera()
cam.release()
cv.destroyAllWindows()
