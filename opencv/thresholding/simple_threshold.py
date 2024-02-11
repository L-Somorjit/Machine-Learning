import cv2
import numpy as np

img = cv2.imread('black_white.png')

# apply thresholding

_, th1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
_, th4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
_, th5 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)




cv2.imshow("original", img)
cv2.imshow("threshold1", th1)
cv2.imshow("threshold2", th2)
cv2.imshow("threshold3", th3)
cv2.imshow("threshold4", th4)
cv2.imshow("threshold5", th5)
cv2.waitKey()
cv2.destroyAllWindows()