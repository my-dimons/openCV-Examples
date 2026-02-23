import cv2 as cv

cam = cv.VideoCapture(0);

frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cam.read();

    cv.imshow('webcam', frame)

    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
