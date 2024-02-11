import cv2
import numpy as np
import matplotlib.pyplot as plt


img =cv2.imread("col_balls.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img = cv2.resize(img, (600, 400))
img_gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, mask = cv2.threshold(img_gray, 230, 255, cv2.THRESH_BINARY_INV)
ero_kernel = np.ones((3,3), np.uint8)
result = cv2.erode(mask, ero_kernel)

dila_kernel = np.ones((3,3), np.uint8)
dila_result =cv2.dilate(mask, dila_kernel)

title = ['ori', 'mask', 'erosion', 'dilation']
images = [img, img_gray, result, dila_result]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([])

plt.show()


# cv2.imshow("original", img)
# cv2.imshow("gray", img_gray)
# cv2.imshow('mask', mask)
# cv2.imshow("erosion", result)
# cv2.imshow("dilation", dila_result)
# cv2.waitKey()
# cv2.destroyAllWindows()
