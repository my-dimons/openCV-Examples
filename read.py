import cv2 as cv

# Read image
img = cv.imread('photos/cat.jpg')

# Open window
cv.imshow('Image recognition', img)

# When the '0' key is pressed, close the window
cv.waitKey(0);