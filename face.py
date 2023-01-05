import cv2#PBL 2
import serial
ArduinoSerial=serial.Serial('com10',9600)
print( "Camera Mode!!")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(1)
            

while video.isOpened():
    check, frame = video.read()
    frame=cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame,scaleFactor=1.1, minNeighbors=5)
    for x,y,w,h in faces:
        string='X{0:d}Y{1:d}'.format((x+w//2),(y+h//2))
        print(string)
        ArduinoSerial.write(string.encode('utf-8'))
        cv2.circle(frame,(x+w//2,y+h//2),2,(0,255,0),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.rectangle(frame,(640//2-30,480//2-30),
                 (640//2+30,480//2+30),
                  (255,255,255),3)
    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
    

