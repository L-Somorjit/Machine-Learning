import cv2


img = cv2.imread('road.jpg',0)
img = cv2.resize(img, (700, 300))
img = cv2.flip(img,1)
print(img.shape)

cv2.imshow('sample', img)

k = cv2.waitKey(0)
if k==ord('s'):
    cv2.imwrite('flip_out.png', img)
else:
    cv2.destroyAllWindows()