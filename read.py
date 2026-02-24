import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
#cv.imshow('blank', blank)

cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=cv.FILLED)
#cv.imshow('rectangle', blank)

cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=3)

cv.line(blank, (0, 0), (250, 300), (255, 0, 0), thickness=3)

blank = cv.cvtColor(blank, cv.COLOR_BGR2GRAY)
blank = cv.GaussianBlur(blank, (101, 101), cv.BORDER_DEFAULT)
#blank = cv.Canny(blank, 125, 175)

cv.imshow('img', blank)
# When any key is pressed, close the window
cv.waitKey(0);