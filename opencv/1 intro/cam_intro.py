import cv2

cap = cv2.VideoCapture(0)

#DIVX, XVID, MJPG, X264, WMV1, WMV2

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("out.avi", fourcc, 20.0, (640, 480),0) #0 if gray

while(cap.isOpened()):
    res, frame = cap.read()
    if res == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.flip(gray, 1)
        cv2.imshow("frame",frame)
        cv2.imshow('gray', gray)
        output.write(gray)

        k=cv2.waitKey(25)
        if k==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()