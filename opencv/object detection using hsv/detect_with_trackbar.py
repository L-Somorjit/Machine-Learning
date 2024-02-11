import cv2
import numpy as np

img = cv2.imread("balls.webp")
img = cv2.resize(img, (400, 300))

def nothing(x):
    pass

cv2.namedWindow("detect colour")

cv2.createTrackbar("lower_h", "detect colour", 0, 255, nothing)
cv2.createTrackbar("lower_s", "detect colour", 0, 255, nothing)
cv2.createTrackbar("lower_v", "detect colour", 0, 255, nothing)

cv2.createTrackbar("higher_h", "detect colour", 255, 255, nothing)
cv2.createTrackbar("higher_s", "detect colour", 255, 255, nothing)
cv2.createTrackbar("higher_v", "detect colour", 255, 255, nothing)


while True:
    l_h = cv2.getTrackbarPos("lower_h", "detect colour")
    l_s = cv2.getTrackbarPos("lower_s", "detect colour")
    l_v = cv2.getTrackbarPos("lower_v", "detect colour")

    h_h = cv2.getTrackbarPos("higher_h", "detect colour")
    h_s = cv2.getTrackbarPos("higher_s", "detect colour")
    h_v = cv2.getTrackbarPos("higher_v", "detect colour")

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([l_h, l_s, l_v])
    uper = np.array([h_h,h_s, h_v])

    mask = cv2.inRange(hsv, lower, uper)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("original", img)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()