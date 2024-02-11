import cv2
import numpy as np


thor = cv2.imread('hero1.jpg')
strom_breaker = cv2.imread('strom_breaker.JPG')

thor = cv2.resize(thor, (800, 500))
strom_breaker = cv2.resize(strom_breaker, (300, 400))

strom_gray = cv2.cvtColor(strom_breaker, cv2.COLOR_BGR2GRAY)

# create masking using threshold select threshold through brut force
_, mask = cv2.threshold(strom_gray, 40, 255, cv2.THRESH_BINARY)

# using mask select boreground

strom_fg = cv2.bitwise_and(strom_breaker, strom_breaker, mask=mask)



l, h, c = strom_breaker.shape
roi = thor[0:l, 0:h]
# create reverse mask of strom breaker, so that it gives 0 and black the region of background

rev_mask = cv2.bitwise_not(mask)

# create space for fg image in back ground

roi_mask = cv2.bitwise_and(roi, roi, mask=rev_mask)

# add bg image in space created

fg_image = cv2.add(roi_mask, strom_fg)


# add to final image

final = thor.copy()
final[0:l, 0:h] = fg_image

cv2.imshow("thor", thor)
cv2.imshow("strom breaker", strom_breaker)
cv2.imshow("strom gray", strom_gray)
cv2.imshow("mask", mask)
cv2.imshow("revmask", rev_mask)
cv2.imshow("strom fg", strom_fg)
cv2.imshow('roi', roi)
cv2.imshow("roi_mask", roi_mask)
cv2.imshow("fg_image", fg_image)
cv2.imshow("final", final)

cv2.waitKey()
cv2.destroyAllWindows()