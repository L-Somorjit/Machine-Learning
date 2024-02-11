import cv2

img1 = cv2.imread("bro_thor.jpg")
img2 = cv2.imread("roi_opr.jpg")


# make size same for blending

img1 = cv2.resize(img1, (300, 400))
img2 = cv2.resize(img2, (300, 400))

# normal add without weightage

result1 = cv2.add(img1, img2)

# blend with weightage

result2 = cv2.addWeighted(src1=img1,alpha=0.5, src2=img2, beta=0.5, gamma=5)

cv2.imshow("img1",img1)
cv2.imshow("img2", img2)
cv2.imshow("result1", result1)
cv2.imshow("result2", result2)

cv2.waitKey()
cv2.destroyAllWindows()