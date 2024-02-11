import cv2
import numpy as np



img = cv2.imread('shapes.png')
img = cv2.resize(img, (400, 500))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass

cv2.namedWindow("threshold")
cv2.createTrackbar("thres", "threshold", 0, 255, nothing)

while True:
    t = cv2.getTrackbarPos("thres", "threshold")
    _, thres = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("threshold", thres)

    if cv2.waitKey(1)==27:
        break

"""
Countour is curve along the boundary following same intensity or colour

draws on white foreground and black background
"""
# RETR_TREE is countour retrieval method, CHAIN_APPROX_SIMPLE is countour approximation method for selecting countour points
cp, _ = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cp is list with countour point


img = cv2.drawContours(img,cp, -1, (0,0,255), 2) # -1 to select all countour index

cv2.imshow("original", img)
cv2.imshow("Gray", gray)
cv2.waitKey()
cv2.destroyAllWindows()