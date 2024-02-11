import cv2
import numpy as np

img = cv2.imread("road.jpg")
img = cv2.resize(img, (640, 350))

# drawing line
img = cv2.line(img=img, pt1=(0,0), pt2=(230, 120), color=(123, 64, 61), thickness=5)

# drawing arrowed line
img = cv2.arrowedLine(img=img, pt1=(0, 125), pt2=(200, 125), color=(6, 245, 120), thickness=5)

# drawing square
img = cv2.rectangle(img=img, pt1=(320, 60), pt2=(440, 120), color=(34, 65, 20), thickness=3)

# drawing circle
img = cv2.circle(img=img, center=(450, 220), radius=50, color=(230, 43, 23), thickness=-3)

# drawing ellipse
img = cv2.ellipse(img=img, center=(450, 220), axes=(60,30), angle=0, startAngle=0, endAngle=240, color=(120,34,65), thickness=3)

# write text
img = cv2.putText(img=img, text="Evening view", org=(0, 330), fontFace=cv2.FONT_ITALIC, fontScale=2, color=(12,230,122), thickness=5)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()