import cv2
import numpy as np


img = cv2.imread('hulk.jpg')

img1 = img.copy()


cv2.imshow("original", img)
for i in range(4):
    img1 = cv2.pyrDown(img1)
    cv2.imshow("result "+str(i), img1)

cv2.waitKey()
cv2.destroyAllWindows()