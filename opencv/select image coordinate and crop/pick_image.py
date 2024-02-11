import cv2

img = cv2.imread('road.jpg')
img = cv2.resize(img, (600,400))

count = 0
coordinate = []

def picking(event, x, y, flags, param):
    global count
    global coordinate
    if count<3 and event==cv2.EVENT_LBUTTONDOWN:
        coordinate.append((x,y))
        count +=1
    elif count==3 and event==cv2.EVENT_LBUTTONDOWN:
        count = 0
        coordinate = []
        coordinate.append((x,y))
        count +=1

  
cv2.namedWindow(winname='pick')
cv2.setMouseCallback('pick', picking)


while True:
    cv2.imshow('pick', img)
    if cv2.waitKey(1)==27:
        break

C1, C2, C3 = coordinate[0], coordinate[1], coordinate[2]
roi = img[C1[1]:C2[1], C1[0]:C2[0]]

row_difference = C2[0]-C1[0]
column_difference = C2[1]-C1[1]

img[C3[1]:C3[1]+column_difference, C3[0]:C3[0]+row_difference]=roi

cv2.imshow("NEW", img)
cv2.waitKey(0)
cv2.destroyAllWindows()