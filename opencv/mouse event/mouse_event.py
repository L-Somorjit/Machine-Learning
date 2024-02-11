import cv2
import numpy as np

def move(event, x, y, flags, param):

    if event==cv2.EVENT_LBUTTONDOWN:
        text = f"x:{x} and y:{y}"
        cv2.putText(img=img, text=text, org=(x,y), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, 
        color=(20,250,40), thickness=1)

    if event==cv2.EVENT_RBUTTONDOWN:
        r = img[y,x,2]
        g = img[y,x,1]
        b = img[y,x,0]
        text = f".B={b}, G={g}, R={r}"
        cv2.putText(img=img, text=text, org=(x,y), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, 
        color=(20,250,40), thickness=1)



cv2.namedWindow(winname="mouse")
cv2.setMouseCallback("mouse", move)

img = cv2.imread('balls.webp')
# img = cv2.resize(img, (600, 400))
while True:
    cv2.imshow("mouse", img)
    
    if cv2.waitKey(1)==27: #esc
        break
cv2.destroyAllWindows()
