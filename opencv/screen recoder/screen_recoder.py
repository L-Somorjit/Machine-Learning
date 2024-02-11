import cv2
import pyautogui as ui
import numpy as np

win = ui.size()
fr = 25

file = input("Enter path for file storage: ")

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter(file, fourcc, fr, win)

# Create recording module

cv2.namedWindow("Screen_Reording", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Screen_Recording",(600, 400))

while True:
    img = ui.screenshot()
    img = np.array(img)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # cv2.imshow("Screen_Recording", img)

    output.write(img)

    if cv2.waitKey(25) == ord("q"):
        break

output.release()
cv2.destroyAllWindows()