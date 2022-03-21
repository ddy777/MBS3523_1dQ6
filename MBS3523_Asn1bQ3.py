import cv2
print(cv2.__version__)

# you may need to change the number inside () to 0 1 or 2,
# depending on which webcam you are using
capture = cv2.VideoCapture(0)
# Below 2 lines are used to set the webcam window size
capture.set(3,640) # 3 is the width of the frame (x-axis)
capture.set(4,480) # 4 is the height of the frame (y-axis)

x = 0 #size of rectangle (location of rectangle)
y = 0 #size of rectangle (location of rectangle)

dx = 5 #moving speed (moving space of each step)
dy = 5 #moving speed (moving space of each step)

#select font
font = cv2.FONT_HERSHEY_SIMPLEX
#insert text
text = 'MBS3523 Assignment 1b-Q3 Name : YIP MUN WAH'
#select color (BGR)
red = (0,0,255)
yellow = (51, 255, 255)
#select size
size = 0.7

# Start capturing and show frames on window named 'Frame'
while True:
    success, img = capture.read()

    cv2.putText(img, text, (30, 30), font, size, red, 2)
    cv2.rectangle(img, (x, y), (x + 50, y + 50), yellow, 5)

    x += dx #way to move of x-axis
    y += dy #way to move of y-axis

    if x > 590 or x < 0: #limit collision of x-axis
        dx = dx * -1 #way to move after collision

    if y > 430 or y < 0: #limit collision of y-axis
        dy = dy * -1 #way to move after collision

    cv2.imshow('webCamera', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
