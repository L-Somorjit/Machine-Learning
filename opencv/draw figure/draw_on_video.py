import cv2
import datetime


cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        text = "width:"+str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+" height:"+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame = cv2.putText(img=frame, text=text,org=(0,20), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(255,255,0), thickness=0)
        date = str(datetime.datetime.now())
        frame = cv2.putText(frame, text=date, org=(0,50), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,color=(255,255,0), thickness=0)
        frame = cv2.rectangle(img=frame, pt1=(120,200), pt2=(180, 300), color=(233,126,240), thickness=2)
        cv2.imshow("video",frame)
        if cv2.waitKey(25)==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()