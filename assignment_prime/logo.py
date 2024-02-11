from vidgear.gears import CamGear
from vidgear.gears.helper import reducer
import cv2
from time import time

options = {"STREAM_RESOLUTION": "480p"}
cap = CamGear(source='https://www.youtube.com/watch?v=hvD8Xr9lrIg&ab_channel=RepublicWorld', stream_mode = True, logging=True, **options).start() # YouTube Video URL as input

class_name = []
class_file = 'coco.names'
with open(class_file, 'rt') as f:
    class_name = f.read().rstrip('\n').split('\n')

path_config = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
path_weight = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(path_weight, path_config)
net.setInputSize(320, 320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

record_flag = 0
# infinite loop
while True:
    
    img = cap.read()
    # read frames

    # check if frame is None
    if img is None:
        #if True break the infinite loop
        break
    
    # do something with frame here
    # frame = reducer(frame, percentage=20)

    class_id,  conf, bbox = net.detect(img, confThreshold=0.5)
    


    try:
        
        for cid, con, box in zip(class_id.flatten(), conf.flatten(), bbox):
            if cid == 1 and record_flag == 0: #and record_flag==0:
                in_time = (cap.stream.get(cv2.CAP_PROP_POS_FRAMES))
                record_flag=1
            elif cid==1 and record_flag==1:
                out_time = cap.stream.get(cv2.CAP_PROP_POS_FRAMES)
            cv2.rectangle(img, box, color=(120,140,25), thickness=2)
            cv2.putText(img, class_name[cid-1], (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX,1,(120,140,25),2)
            cv2.putText(img, str(round(con*100, 2)), (box[0]+10, box[1]+150), cv2.FONT_HERSHEY_COMPLEX,1,(120,140,25),2)
    except:
        pass

    img = cv2.resize(img, (1240,840))
    
    cv2.imshow("Output Frame", img)
    # Show output window

    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        #if 'q' key-pressed break out
        break

cv2.destroyAllWindows()
# close output window

# safely close video cap.
cap.stop()

print("In time for person is {} and out time is {}.".format(in_time, out_time))

