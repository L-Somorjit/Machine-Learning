import cv2
import numpy as np


img = cv2.imread('shapes.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (400,600))
gray = cv2.resize(gray, (400,600))

def nothing(x):
    pass

cv2.namedWindow("thre")
cv2.createTrackbar("threshold", "thre", 0, 255, nothing)

while True:
    t = cv2.getTrackbarPos("threshold","thre")
    _, thre = cv2.threshold(gray,t, 255,cv2.THRESH_BINARY_INV)
    cv2.imshow("thre", thre)
    if cv2.waitKey(1)==27:
        break

cntr, heir = cv2.findContours(thre, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Moment helps in finding center of mass, area, etc
"""
MOMENT
"""
c = cntr[0]
m = cv2.moments(c)
print(m)

# centroid x=(m10/m00) y=(m01/m00)
x=int(m['m10']/m['m00'])
y=int(m['m01']/m['m00'])

print(x,y)

"""
AREA

m00 of moment gives area, also cv.CountourArea gives area of specific countou point
"""

print("countour area", cv2.contourArea(c))
print("moment area", m['m00'])

"""
cv.arcLength(), to perimeter or arc, pass another perimeter True if closed
"""
perimeter = cv2.arcLength(c, True)
print(perimeter)
"""
countour approximation, it is used to fix irregular shape
"""

for c in cntr:
    M = cv2.moments(c)
    xc = int(M['m10']/M['m00'])
    yc = int(M['m01']/M['m00'])
    cv2.circle(img, (xc,yc),4,(220, 23, 12), -1)
    cv2.putText(img, "centroid", (xc-15, yc-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (34, 10, 220),1)

    epsilon = 0.01*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)


    hull = cv2.convexHull(approx)

    x1,y1,x2,y2 = cv2.boundingRect(hull)

    cv2.rectangle(img, (x1, y1), (x1+x2, y1+y2), (1, 1, 1),2)


cv2.drawContours(img, cntr, -1, (0,0,255), 2)
cv2.imshow("result", img)
cv2.waitKey()
cv2.destroyAllWindows()