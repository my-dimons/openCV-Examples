# Welcome to OpenCV-Testing!
This is a repo where I mess around in openCV. I thought it would be useful to make a collection of different things possible with openCV, so below are some useful branches that could help you understand openCV!

If you want to contribute to this project, that being a small improvement, better commenting, or an entirely new feature, **GO FOR IT!** I appreciate any form of contribution

## [main](https://github.com/my-dimons/openCV-Testing)
A **very** basic program that just reads and displays an image. Has a rescale function to resize the image.

## [read-video](https://github.com/my-dimons/openCV-Testing/tree/read-video)
Plays a video at 30fps and rescales the frame to 0.75x the original size

## [webcam](https://github.com/my-dimons/openCV-Testing/tree/webcam)
Gets the users webcam and plays it back. Has some post proccessing options and many other functions. Displays the webcam FPS in the top left.

## [draw-shape](https://github.com/my-dimons/openCV-Testing/tree/draw-shape)
Shows how to draw shapes and do some post processing

## [object-tracking](https://github.com/my-dimons/openCV-Testing/tree/object-tracking)
Uses openCV's haarcascades to recognize faces and eyes. Not very accurate.

## [yolov5-tracking](https://github.com/my-dimons/openCV-Testing/tree/yolov5-tracking)
***NOTE: REQUIRES [YOLOv5](https://github.com/ultralytics/yolov5).*** Using yolov5, uses the users webcam and recognizes objects. 
Objects that are recognized with **>50%** confidence get a green box around them, and some text saying what the object is and the confidence %.

## [desktop-video-feed](https://github.com/my-dimons/openCV-Testing/tree/desktop-video-feed)
Displays the users desktop as a video feed using [pyautogui](https://pypi.org/project/PyAutoGUI/) and a conversion function.

## [text-recognition `WIP`](https://github.com/my-dimons/openCV-Testing/tree/text-recognition)
Using the users desktop as a video feed, using [pyautogui](https://pypi.org/project/PyAutoGUI/) and [pytesseract](https://pypi.org/project/pytesseract/) ([GitHub](https://github.com/tesseract-ocr/tesseract)) it recognizes text.
Recognized text is given a blue outline and printed in the terminal.
