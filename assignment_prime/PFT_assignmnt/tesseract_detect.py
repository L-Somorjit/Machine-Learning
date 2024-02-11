import cv2
import pytesseract

cap = cv2.VideoCapture('4.mp4')

while True:
    
    rep, img = cap.read()
    # read frames

    if rep == True:

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        print(pytesseract.image_to_string(img_rgb))

        print("*"*100)
    
        cv2.imshow("Output Frame", img)
        # Show output window

        key = cv2.waitKey(30) & 0xFF
        # check for 'q' key-press
        if key == ord("q"):
            #if 'q' key-pressed break out
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
# close output window

# safely close video cap.
