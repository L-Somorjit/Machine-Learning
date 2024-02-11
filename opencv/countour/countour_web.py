import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cv2.namedWindow('Select Colour', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Select Colour',(300,300))
def nothing(x):
    pass

cv2.createTrackbar('lower h', 'Select Colour', 0, 255, nothing)
cv2.createTrackbar('lower s', 'Select Colour', 0, 255, nothing)
cv2.createTrackbar('lower v', 'Select Colour', 0, 255, nothing)
cv2.createTrackbar('higher h', 'Select Colour', 255, 255, nothing)
cv2.createTrackbar('higher s', 'Select Colour', 255, 255, nothing)
cv2.createTrackbar('higher v', 'Select Colour', 255, 255, nothing)
cv2.createTrackbar('thresh', 'Select Colour', 0, 255, nothing)

while True:
    _, frame = cap.read()
    frame= cv2.resize(frame,(300, 300))
    frame = cv2.medianBlur(frame, 5)
    lh = cv2.getTrackbarPos('lower h', 'Select Colour')
    ls = cv2.getTrackbarPos('lower s', 'Select Colour')
    lv = cv2.getTrackbarPos('lower v', 'Select Colour')
    hh = cv2.getTrackbarPos('higher h', 'Select Colour')
    hs = cv2.getTrackbarPos('higher s', 'Select Colour')
    hv = cv2.getTrackbarPos('higher v', 'Select Colour')
    lower = np.array([lh, ls, lv])
    higher = np.array([hh, hs, hv])

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, higher)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    mask_in = cv2.bitwise_not(mask)
    cntr, heir = cv2.findContours(mask_in, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(result, cntr, -1, (0,0,255), 2)
    cv2.imshow('Original', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('mask inverse', mask_in)
    cv2.imshow('result', result)
    if cv2.waitKey(1)==27:
        break