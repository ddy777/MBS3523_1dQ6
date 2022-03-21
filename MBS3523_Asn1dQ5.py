import cv2
import numpy as np

cam = cv2.VideoCapture(0)

text = "MBS3523 Assignment 1d-Q5 Name: YIP MUN WAH"
font = cv2.FONT_HERSHEY_SIMPLEX
red = (0,0,255)
blue = (255, 0, 0)
size = 0.5
thickness = int(1.8)
line_thick = 2

def non(x):
    pass

cv2.namedWindow('webCamera')

cv2.createTrackbar('X_POS','webCamera',320,640,non)
cv2.createTrackbar('Y_POS','webCamera',240,480,non)

while True:
    success, img = cam.read()

    x = cv2.getTrackbarPos('X_POS', 'webCamera')
    y = cv2.getTrackbarPos('Y_POS', 'webCamera')

    cv2.line(img, (x, 0), (x, 480), blue, line_thick)
    cv2.line(img, (0, y), (640, y), blue, line_thick)

    cv2.putText(img, text, (100, 30), font, size, red, thickness)

    cv2.imshow('webCamera', img)
    if cv2.waitKey(1) & 0xff == 27: #press "ESC"
        break

cv2.destroyAllWindows()
