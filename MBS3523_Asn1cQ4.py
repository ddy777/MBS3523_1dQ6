import cv2
print(cv2.__version__)

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

font = cv2.FONT_HERSHEY_SIMPLEX
text = 'MBS3523 Assignment 1c-Q4 Name : YIP MUN WAH'
red = (0,0,255)
size = 0.7

while True :
    unuse, img = cam.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 3)

    for (x, y, a, b) in faces :
        cv2.rectangle(img, (x, y), (x + a, y + b), (0, 255, 0), 2)

        # y to y+b and x to x+a is the area of face deatected
        imgGray [y : y+b, x : x+a] = img [y : y+b, x : x+a]

    cv2.putText(imgGray, text, (30, 30), font, size, red, 2)

    cv2.imshow('webCamera', imgGray)

    if cv2.waitKey(1) & 0xff == 27 : #press ESC to close
        break

cam.release()
cv2.destroyAllWindows()
