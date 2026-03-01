import cv2 as cv
import time

capture = cv.VideoCapture('videos/kitten.mp4')

# Amount of seconds to wait to achieve 30fps
FPS = 1 / 30

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    receievedImage, frame = capture.read()

    # Check if an image was recieved
    if receievedImage == False:
        break

    frame_resized = rescaleFrame(frame)
    
    # Show the current frame of the video
    cv.imshow('video', frame_resized)

    # Sleep to achieve the FPS count
    time.sleep(FPS)

    # If the 'q' key is pressed, close the window
    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()