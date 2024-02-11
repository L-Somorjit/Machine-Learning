import cv2

cap = cv2.VideoCapture('sampl.mp4')

rep, frame = cap.read()
count=1

while True:
    if rep==True:

        cv2.imwrite("C:\\Users\\leich\\Desktop\\Somorjit code\\opencv\\frames\img_%d.jpg"%count, frame)
        cap.set(cv2.CAP_PROP_POS_MSEC, (count*100))
        rep, frame = cap.read()

        cv2.imshow('image', frame)
        count += 1

        if cv2.waitKey(1) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()