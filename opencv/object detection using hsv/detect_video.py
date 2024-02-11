import cv2
import numpy as np


cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('detection')
cv2.createTrackbar("lower_h", "detection", 0, 255, nothing)
cv2.createTrackbar("lower_s", "detection", 0, 255, nothing)
cv2.createTrackbar("lower_v", "detection", 0, 255, nothing)

cv2.createTrackbar("higher_h", "detection", 255, 255, nothing)
cv2.createTrackbar("higher_s", "detection", 255, 255, nothing)
cv2.createTrackbar("higher_v", "detection", 255, 255, nothing)

while True:
    res, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("lower_h", "detection")
    l_s = cv2.getTrackbarPos("lower_s", "detection")
    l_v = cv2.getTrackbarPos("lower_v", "detection")

    h_h = cv2.getTrackbarPos("higher_h", "detection")
    h_s = cv2.getTrackbarPos("higher_s", "detection")
    h_v = cv2.getTrackbarPos("higher_v", "detection")

    mask = cv2.inRange(hsv,(l_h,l_s,l_v), (h_h, h_s, h_v))
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("original",frame)
    cv2.imshow("result", result)

    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()