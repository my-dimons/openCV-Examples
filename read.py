import cv2 as cv
import pytesseract as pyt
import pyautogui as pag

pyt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

image = rescaleFrame(pag.screenshot(), 0.5)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Extract text 
extracted_text = pyt.image_to_string(gray)

print("Extracted Text: \n" + extracted_text)


data = pyt.image_to_data(image, output_type=pyt.Output.DICT)

n_boxes = len(data['level'])
for i in range(n_boxes):
    (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
    cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)



cv.imshow("Recognized Text", image)

cv.waitKey(0)