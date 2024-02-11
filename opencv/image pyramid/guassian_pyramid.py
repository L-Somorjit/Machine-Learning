import cv2
import numpy as np


img = cv2.imread('hulk.jpg')

"""
Image pyramid is creating different resolutions of the same image

It is use in object detection and image blending

There are two types:
    1) Guassian pyramid
    2) Laplacian pyramid
"""
# We will discuss only guassian, we can do pyramid up or pyramid down

pd1 = cv2.pyrDown(img)
pd2 = cv2.pyrDown(pd1)


pu1 = cv2.pyrUp(pd2) #pyramid up doesn't increase resolution

cv2.imshow("original", img)
cv2.imshow("pd1", pd1)
cv2.imshow("pd2", pd2)
cv2.imshow("pu1", pu1)

cv2.waitKey()
cv2.destroyAllWindows()