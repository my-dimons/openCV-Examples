import cv2 as cv
import pytesseract as pyt
import pyautogui as pag
import numpy as np

pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def convertScreenshotToFrame(screenshot):
    frame = np.array(screenshot)
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

    return frame

while True:
    frame = rescaleFrame(convertScreenshotToFrame(pag.screenshot()), 0.5)

    cv.imshow("Desktop", frame)

    if cv.waitKey(1) == ord('q'):
        break
    
cv.destroyAllWindows()