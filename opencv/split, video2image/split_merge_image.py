import cv2

img = cv2.imread('road.jpg')

img = cv2.resize(img, (600,400))
print("shape ", img.shape)
print("size ", img.size)

"""
splitting image channel to R,G,B
"""
b,g,r = cv2.split(img)


"""
Merging channels to single image
"""
merge = cv2.merge((b,g,r))


# cv2.imshow('Original', img)
# cv2.imshow("Merged", merge)
# cv2.imshow("B", b)
# cv2.imshow("G", g)
# cv2.imshow("R", r)

"""
selct image pixel
"""
pick = img[230, 400]
B = img[230, 400, 0]
G = img[230, 400, 1]
R = img[230, 400, 2]
print(pick)
print('B: ',B)
print('G: ',G)
print('R: ',R)
cv2.waitKey()
cv2.destroyAllWindows()