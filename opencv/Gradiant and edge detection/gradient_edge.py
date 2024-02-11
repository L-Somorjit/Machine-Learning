import cv2
import numpy as np


img = cv2.imread("passport.jpg", 0)
img = cv2.resize(img, (600, 400))

# Sobel edge detection join guassian smoothing and derivative
# direction of derivate can be specified along x or y

# using ddepth CV_8U or default, change -ve value to 0, so no proper edge is found
# using higher CV_64F and usde absolute to change to uint8 for better edge

sobel_x_u8 = cv2.Sobel(src=img, ddepth=cv2.CV_8U , dx=1, dy=0, ksize=3)
sobel_x = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=3)
sobel_x = np.uint8(np.absolute(sobel_x))

sobel_y = cv2.Sobel(img, cv2.CV_64F,0,1,ksize=3)
sobel_y = np.uint8(np.absolute(sobel_y))

sobel_combine = cv2.bitwise_or(sobel_x, sobel_y)


# in sobel if ksize is -1, it used scharr filter

scharr = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=-1)
scharr = np.uint8(np.absolute(scharr))


# laplacian calculates the leplacian of the image

laplacian = cv2.Laplacian(src=img, ddepth=cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

# Canny edge detection perform many other function including noise removal, gaussian intensity, double threshold

canny = cv2.Canny(image=img, threshold1=35, threshold2=200)

cv2.imshow("Gray", img)
cv2.imshow("sobelx8u",sobel_x_u8)
cv2.imshow("sobelX", sobel_x)
cv2.imshow("sobelY", sobel_y)
cv2.imshow("sobel combine", sobel_combine)
cv2.imshow('scharr', scharr)
cv2.imshow('leplacian', laplacian)
cv2.imshow('canny', canny)



# canny with trackbar

def nothing(x):
    pass

cv2.namedWindow('Canny')
cv2.createTrackbar('threshold', 'Canny', 0, 255, nothing)

while True:
    t = cv2.getTrackbarPos('threshold', 'Canny')
    res = cv2.Canny(image=img, threshold1=t, threshold2=255)
    cv2.imshow("Canny", res)
    if cv2.waitKey(1)==27:
        break
# cv2.waitKey()
cv2.destroyAllWindows()