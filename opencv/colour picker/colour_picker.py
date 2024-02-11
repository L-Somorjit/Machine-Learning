import cv2
import numpy as np


def cross(x):
    pass

img = np.zeros((300,512,3), np.uint8)

cv2.namedWindow(winname="Colour Picker")

k="0:OFF 1:ON"
cv2.createTrackbar(k, "Colour Picker", 0, 1, cross)
cv2.createTrackbar("R", "Colour Picker", 0, 255, cross)
cv2.createTrackbar("G", "Colour Picker", 0, 255, cross)
cv2.createTrackbar("B", "Colour Picker", 0, 255, cross)

while True:
    cv2.imshow("Colour Picker", img)

    if cv2.waitKey(1)==27:
        break

    s = cv2.getTrackbarPos(k,"Colour Picker")
    r = cv2.getTrackbarPos("R", "Colour Picker")
    g = cv2.getTrackbarPos("G", "Colour Picker")
    b = cv2.getTrackbarPos("B", "Colour Picker")
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()