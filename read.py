import cv2 as cv
import time

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

video = cv.VideoCapture(0)
fps = 1 / 30

while True:
    ret, frame = video.read()

    if not ret:
        break

    faces = face_cascade.detectMultiScale(frame, 1.1, 2)
    eyes = eye_cascade.detectMultiScale(frame, 1.1, 2)

    for(x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    for(x, y, w, h) in eyes:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv.imshow("window", frame)

    time.sleep(fps)

    if cv.waitKey(1) == ord('q'):
        break

video.release()
cv.destroyAllWindows()