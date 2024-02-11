import cv2
import numpy as np


img1 = np.zeros((300,400,3),np.uint8)
img1 = cv2.rectangle(img1, (30,90), (140, 220), (255,255,255), -1)

img2 = np.zeros((300,400,3), np.uint8)
img2 = cv2.rectangle(img2, (3,100), (250, 150), (255, 255, 255), -1)

andbit = cv2.bitwise_and(img1, img2)
orbit = cv2.bitwise_or(img1, img2)
notimg1 = cv2.bitwise_not(img1)
notimg2 = cv2.bitwise_not(img2)
xorbit = cv2.bitwise_xor(img1, img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("andbit", andbit)
cv2.imshow("orbit", orbit)
cv2.imshow("not1", notimg1)
cv2.imshow("not2", notimg2)
cv2.imshow("XOR", xorbit)
cv2.waitKey()
cv2.destroyAllWindows()