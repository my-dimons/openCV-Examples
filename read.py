import numpy as np
import cv2 as cv
import time
import constants as consts

cam = cv.VideoCapture(0)

frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

prev_frame_time = 0
new_frame_time = 0

def rescale_frame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def calculate_fps():
    global prev_frame_time
    new_frame_time = time.time()

    fps = "FPS: " + str(int(1 / (new_frame_time - prev_frame_time)))
    prev_frame_time = new_frame_time

    print(fps)
    return fps

def put_fps_text(frame, fps, position):
    font = cv.QT_FONT_NORMAL

    cv.putText(frame, fps, position, font, consts.FPS_TEXT_SCALE, consts.FPS_TEXT_COLOR, 1, cv.LINE_AA)

def process_image(frame):
    processed_frame = frame

    if (consts.APPLY_BLUR):
        processed_frame = cv.GaussianBlur(processed_frame, (consts.BLUR_AMOUNT, consts.BLUR_AMOUNT), cv.BORDER_DEFAULT)

    if (consts.APPLY_CANNY):
        processed_frame = cv.Canny(processed_frame, consts.CANNY_THRESHOLD_1, consts.CANNY_THRESHOLD_2)

    if (consts.MIRROR_IMAGE):
        processed_frame = cv.flip(processed_frame, 1)
        
    return processed_frame

def read_camera():
    while True:
        ret, frame = cam.read() 

        if ret == False:
            break

        fps = calculate_fps()

        resized_frame = rescale_frame(frame, consts.WEBCAM_RESIZE)
        processed_frame = process_image(resized_frame)

        put_fps_text(processed_frame, fps, consts.FPS_TEXT_POS)

        cv.imshow('webcam', resized_frame)  
        cv.imshow('processed webcam', processed_frame)

        if cv.waitKey(1) == ord('q'):
            break

read_camera()
cam.release()
cv.destroyAllWindows()