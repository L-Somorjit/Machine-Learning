import cv2
import numpy as np


img1 = cv2.imread("bro_thor.jpg")
img2 = cv2.imread("roi_opr.jpg")

img1 = cv2.resize(img1, (400, 500))
img2 = cv2.resize(img2, (400, 500))

def blend(x):
    pass

img = np.zeros((400, 500), np.uint8)
cv2.namedWindow("win")

switch = "0:OFF, 1:ON"
cv2.createTrackbar(switch, "win",0, 1, blend)
cv2.createTrackbar("alpha", "win", 1, 100, blend)

while True:
    s = cv2.getTrackbarPos(switch, "win")
    a = cv2.getTrackbarPos("alpha", "win")
    n = a/100

    if s==0:
        dst = img[:]
    else:
        dst = cv2.addWeighted(src1=img1, alpha=n, src2=img2, beta=1-n, gamma=0)
        cv2.putText(dst, text=str(a), org=(0, 20), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(123,234,236),
        thickness=1)
    cv2.imshow("dst", dst)
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()