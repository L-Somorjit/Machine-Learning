import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("girl.jpg", 0)
img = cv2.resize(img, (300,300))

kernel = np.ones((3,3), np.uint8)
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

# opening is erosion followed by dilation
o = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# closing is dilation followed by erosion

c = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# top head is difference between mask and opening
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

# Gradient is difference between dilation and erosion

gr = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

# Black is difference between closing and input

bh = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)

e = cv2.morphologyEx(mask, cv2.MORPH_ERODE, kernel)

d = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

images = [img, mask, o, c, th, gr, bh, e, d]
titles = ['ori', 'mask', 'opening', 'closing', 'tophead', 'gradient', 'blackhead', 'errode', 'dilation']


for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()


# cv2.imshow("gray", img)
# cv2.imshow('mask', mask)
# cv2.imshow('opening', o)
# cv2.imshow('closing', c)




# cv2.waitKey()
# cv2.destroyAllWindows()