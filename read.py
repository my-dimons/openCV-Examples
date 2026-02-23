import cv2 as cv

cam = cv.VideoCapture(0);

frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))

#fourcc = cv.VideoWriter_fourcc(*'mp4v')
#out = cv.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))


ret, frame = cam.read();

#out.write(frame)

cv.imshow('webcam', frame)

# When the '0' key is pressed, close the window
cv.waitKey(0);