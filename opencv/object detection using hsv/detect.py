import cv2
import numpy as np


img = cv2.imread("balls.webp")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

u_c = np.array([142,255,255])
l_c = np.array([92,156,85])

# creat mask
mask = cv2.inRange(hsv, l_c, u_c)

result = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("balls", result)

cv2.waitKey()
cv2.destroyAllWindows()