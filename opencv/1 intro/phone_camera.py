import cv2

camera = "https://192.168.29.140:8080/video"

cap = cv2.VideoCapture(0)
cap.open(camera)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("phone_camera.mp4",fourcc, 20.0, (640, 480))

while cap.isOpened():

    res, frame = cap.read()
    if res == True:
        

        # frame = cv2.resize(frame, (640, 400))
        cv2.imshow("phone", frame)
        output.write(frame)

        k=cv2.waitKey(20)
        if k==ord("q"):
            break
cap.release()
output.release()
cv2.destroyAllWindows