import cv2
import pytesseract
from pytesseract import Output

cap = cv2.VideoCapture('ply.mp4')

flag_75 = 0
start_75 = 0
stop_75 = 0
flag_ply = 0
start_ply = 0
stop_ply = 0

def check_75_text(img):
    text_obj = pytesseract.image_to_data(img, lang="eng", config="--psm 6 --oem 3", output_type=Output.DICT)
    text = (text_obj['text'])
    text = [i for i in text if i]
    print(text)
    if '75' in text or '[75]' in text or 'INDIA' in text:
        return True
    else:
        return False

def check_ply(img):
    text_obj = pytesseract.image_to_data(img, lang="eng", output_type=Output.DICT)
    text = (text_obj['text'])
    text = [i for i in text if i]
    if 'CenturyPly' in text or 'CENTURYPLY' in text or  'FIREWALL' in text:
        return True
    else:
        return False


while True:
    
    rep, img = cap.read()
    # read frames

    if rep == True:

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


        if check_75_text(img_rgb) and flag_75==0:
            start_75 = cap.get(cv2.CAP_PROP_POS_FRAMES)
            flag_75=1
        elif check_75_text(img_rgb) and flag_75==1:
            stop_75 = cap.get(cv2.CAP_PROP_POS_FRAMES)

        if check_ply(img_rgb) and flag_ply==0:
            start_ply = cap.get(cv2.CAP_PROP_POS_FRAMES)
            flag_ply=1
        elif check_ply(img_rgb) and flag_ply==1:
            stop_ply = cap.get(cv2.CAP_PROP_POS_FRAMES)

        
        cv2.imshow("Output Frame", img)
        # Show output window

        key = cv2.waitKey(1) & 0xFF
        # check for 'q' key-press
        if key == ord("q"):
            #if 'q' key-pressed break out
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()

if start_75 != 0:
    print("Logo 75 start time: {} and stop time: {}".format(start_75, stop_75))
else:
    print("Logo 75 not found")

if start_ply != 0:
    print("Century ply in time: {} and out time: {}".format(start_ply, stop_ply))
else:
    print("Century ply not found")
# close output window

# safely close video cap.
