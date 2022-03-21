import cv2
import numpy as np

EVT = 0

text = "MBS3523 Assignment 1d-Q5 Name: YIP MUN WAH"
font = cv2.FONT_HERSHEY_SIMPLEX
red = (0,0,255)
blue = (255, 0, 0)
size = 0.5
text_thick = int(1.8)
thickness = 3

# mouse callback function
def draw_rectangle(event, x, y, flags, param) :
    global PNT1
    global PNT2
    global EVT

    if event == cv2.EVENT_LBUTTONDOWN:
        PNT1 = (x,y)
        EVT = event
        print(event)
        print(PNT1)

    if event == cv2.EVENT_LBUTTONUP:
        PNT2 = (x,y)
        EVT = event
        print(PNT2)

    if event == cv2.EVENT_RBUTTONUP: # RBUTTONUP --> event = 5
        EVT = event
        print(event)

cv2.namedWindow('webCamera')
cv2.setMouseCallback('webCamera',draw_rectangle)

cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()

    if EVT == 4:
        cv2.rectangle(img, PNT1, PNT2, blue, thickness)
        img1 = img[PNT1[1]:PNT2[1], PNT1[0]:PNT2[0]] #chopped image displacment
        cv2.imshow('chopped image', img1)

    if EVT == 5:
        img[:,:] = img #keep the orgin image
        cv2.destroyWindow('chopped image') #close the chopped image
        EVT = 0

    cv2.putText(img, text, (100, 30), font, size, red, text_thick)

    cv2.imshow('webCamera',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
