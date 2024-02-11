import pafy

import cv2
url = "https://www.youtube.com/watch?v=H6BRZLmY_DY&ab_channel=ABCNews"
data = pafy.new(url)

data = data.getbest(preftype="mp4")

cap = cv2.VideoCapture(data)

while cap.isOpened():
    ret, frame = cap.read()

    cv2.imwrite(frame)

    if cv2.waitKey(20) == ord('k'):
        break
cap.release()
cv2.destroyAllWindows()