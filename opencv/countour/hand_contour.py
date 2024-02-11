import cv2
import numpy as np


img = cv2.imread('hand.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (500,600))
gray = cv2.resize(gray, (500,600))

# def nothing(x):
#     pass

# cv2.namedWindow('threshold')
# cv2.createTrackbar('th', 'threshold',0,255,nothing)

# while True:
#     t = cv2.getTrackbarPos('th','threshold')
#     _, thres = cv2.threshold(gray,t, 255,cv2.THRESH_BINARY_INV)
#     cv2.imshow('thres', thres)
#     if cv2.waitKey(1)==27:
#         break

# blur to remove noise, and draw continours contour, can explore dilation also
gray = cv2.medianBlur(gray, 11)
    
_, thres = cv2.threshold(gray,242, 255,cv2.THRESH_BINARY_INV)

cntr, heir = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

c=cntr[0]
epsilon = 0.001*cv2.arcLength(c, True)
approx = cv2.approxPolyDP(c, epsilon, True)
hull = cv2.convexHull(approx)
cv2.drawContours(img, [c], -1, (12, 34,245), 3)
cv2.drawContours(img, [hull], -1, (12, 234,45), 3)

"""
Convexity defect is the devition of convex hull from countour

so measure between contour and convex hull point indices

returns array of [start point, end point, farthest point, approx distance of to farthest point]
"""

hull2 = cv2.convexHull(c, returnPoints=False) # default True returns coordinate, false return indices
defect = cv2.convexityDefects(c, hull2)

for i in range(defect.shape[0]): # defect is 3D list [no, 0, (start, end, farthest, approx distance)]
    s, e, f, apprx = defect[i][0]
    start = tuple(c[s][0]) # point for the starting
    end = tuple(c[e][0])
    far = tuple(c[f][0])
    cv2.circle(img, far, 2, (255,0,0), 2)

cmax = max(cntr, key=cv2.contourArea)
# print((cmax[:,:,0]).argmax())
cv2.imshow('img',img)
# cv2.imshow('gray', gray)
cv2.imshow('thres', thres)

cv2.waitKey()
cv2.destroyAllWindows()