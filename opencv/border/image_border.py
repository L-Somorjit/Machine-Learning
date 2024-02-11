import cv2


img = cv2.imread("road.jpg")


img = cv2.resize(img, (600,400))

img = cv2.copyMakeBorder(img, top=15, bottom=15, left=15, right=15, borderType=cv2.BORDER_ISOLATED, value=[124,230,230])

cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()