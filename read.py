import cv2 as cv
import time
import torch
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=FutureWarning) # Suppress random deprecation warnings in used scripts 

model = torch.hub.load("ultralytics/yolov5", "yolov5s", trust_repo=True)

if model:
    print("Model Loaded Properly!")
else:
    print("ERROR LOADING MODEL")

video = cv.VideoCapture(0)
fps = 1 / 30

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # Getting results
    results = model(frame)
    labels, cord = results.xyxyn[0][:, -1].numpy(), results.xyxyn[0][:, :-1].numpy()

    # Going through every object
    for i in range(len(labels)):
        row = cord[i]

        confidence = row[4]

        # Check probability of object being correctly identified
        if confidence >= 0.5:
            x1, y1, x2, y2 = (
                int(row[0] * frame.shape[1]), 
                int(row[1] * frame.shape[0]),
                int(row[2] * frame.shape[1]),
                int(row[3] * frame.shape[0])
            )

            width, height = x2 - x1, y2 - y1
            
            label = model.names[int(labels[i])]

            if label == "person":
                print(f"PERSON FOUND AT: x: {x1}, y: {y1}")

            # Label & Shape
            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv.putText(frame, 
                       f'{label}: {(confidence * 100):.2f}%', 
                       (x1, y1 - 10), 
                       cv.FONT_HERSHEY_SIMPLEX, 
                       0.7, 
                       (36, 255, 12), 
                       2)

    cv.imshow("Yolov5 Object Detection", frame)

    if cv.waitKey(1) == ord('q'):
        break

video.release()
cv.destroyAllWindows()