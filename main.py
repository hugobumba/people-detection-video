import cv2
import numpy as np
import imutils

# VIDEO READING
video = cv2.VideoCapture("people2.mp4")

# HOG DESCRIPTOR
HOG = cv2.HOGDescriptor()
HOG.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# OPERATIONS ON THE VIDEO
while True:
    success, frame = video.read()
    if success:
        height, width = frame.shape[:2]
        frame = cv2.resize(frame, (width - (width * 50 // 100), height - (height * 50 // 100)))
        frame_copy = frame.copy()

        # IMAGE READING AND PRE-PROCESSING
        width = frame_copy.shape[1]
        max_width = 500
        if width > max_width:
            frame_copy = imutils.resize(frame_copy, width=max_width)

        # PEDESTRIAN DETECTOR
        pedestrians, weights = HOG.detectMultiScale(frame_copy, winStride=(16, 16), padding=(4, 4), scale=1.03)
        pedestrians = np.array([[x, y, x + w, y + h] for (x, y, w, h) in pedestrians])

        # BOX DRAWING
        count = 1
        for x, y, w, h in pedestrians:
            cv2.rectangle(frame_copy, (x, y), (w, h), (0, 255, 0), 2)
            cv2.rectangle(frame_copy, (x, y - 20), (w, y), (0, 255, 0), -1)
            cv2.putText(frame_copy, f'Person{count}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
            count += 1

        cv2.putText(frame_copy, f'Total: {count-1}', (10, 270), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # RESULT SHOWING
        cv2.imshow("PEDESTRIAN DETECTION", frame_copy)
    else:
        break
    if cv2.waitKey(1) & 0xFF == '9':
        break
