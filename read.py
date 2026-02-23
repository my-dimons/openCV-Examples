import cv2 as cv

# Read image
img = cv.imread('photos/cat_large.jpg')

# Open window
cv.imshow('Image recognition', img)

# When any key is pressed, close the window
cv.waitKey(0);