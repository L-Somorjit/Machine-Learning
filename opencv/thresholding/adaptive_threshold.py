import cv2
import numpy as np

img = cv2.imread('page.jpg',0)

# apply thresholding

_, th1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)




cv2.imshow("original", img)
cv2.imshow("simple", th1)
cv2.imshow("mean adaptive", th2)
cv2.imshow("mean gaussian", th3)
cv2.waitKey()
cv2.destroyAllWindows()