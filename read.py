import cv2 as cv

# Read image
img = cv.imread('photos/cat_large.jpg')

# Open window
cv.imshow('Image recognition', img)

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# When any key is pressed, close the window
cv.waitKey(0);