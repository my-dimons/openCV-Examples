import cv2 as cv

capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('video', frame)

    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()