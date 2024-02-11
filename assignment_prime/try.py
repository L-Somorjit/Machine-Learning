import cv2
import numpy as np

# img = cv2.imread('lenna.png')
# img = cv2.resize(img, (420,420))

cap = cv2.VideoCapture('sample.mp4')

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

while True:

    sucess, img = cap.read()
    class_id,  conf, bbox = net.detect(img, confThreshold=0.5)
    timestamps = [cap.get(cv2.CAP_PROP_POS_MSEC)]
    print(timestamps)

    try:

        for cid, con, box in zip(class_id.flatten(), conf.flatten(), bbox):
            cv2.rectangle(img, box, color=(120,140,25), thickness=2)
            cv2.putText(img, str(round(con*100,2)), class_name[cid-1], (box[0]+10, box[1]+30), cv2.FONT_HERSHEY_COMPLEX,1,(120,140,25),2)
    except:
        pass



    cv2.imshow('lenna', img)
    cv2.waitKey(1)