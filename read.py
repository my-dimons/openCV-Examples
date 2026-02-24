import cv2 as cv

# Read image
img = cv.imread('photos/park.jpg')

img = cv.Canny(img, 125, 175)


def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img, 1.5)

# Open window
cv.imshow('Image recognition', img)

# When any key is pressed, close the window
cv.waitKey(0);