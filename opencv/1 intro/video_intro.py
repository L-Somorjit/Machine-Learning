import cv2
import pyautogui as ui

win = ui.size()
fr = 25

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("1.mp4", fourcc, fr, win)

cap = cv2.VideoCapture('AVSEQ04.DAT')

while(True):
    res, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("frame",frame)
    # cv2.imshow('gray', gray)
    output.write(frame)

    k=cv2.waitKey(25)
    if k==ord('q'):
        break
cap.release()
output.release()
cv2.destroyAllWindows()