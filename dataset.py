import datetime
import numpy as np
import time

import cv2


now = datetime.datetime.now()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

id = raw_input('enter user id')

sampleN=0;

now = time.time()
future = now + 30

while 1:
    while time.time() < future:
     ret, img = cap.read()
    
   
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

     for (x,y,w,h) in faces:

        sampleN=sampleN+1;
  #str(now)

        cv2.imwrite("dataset/User."+str(id)+ "." +str(sampleN) +".jpg", gray)

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.waitKey(100)

        cv2.imshow('img',img)
        if sampleN > 40:

          break
     break
    print("Time exceeded")
   
    cv2.waitKey(1)

    

cap.release()

cv2.destroyAllWindows()


