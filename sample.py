import numpy as np

import cv2
import pickle

import time


f = open('store.pckl', 'rb')
id = pickle.load(f)
f.close()



face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
frame_set=[]
start_time=time.time()

while(True):

    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    frame_set.append(gray)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        cv2.imwrite("User."+str(id)+ "." +".jpg", gray[y:y+h, x:x+w])
        id+=1
        f = open('store.pckl', 'wb')
        pickle.dump(id, f)
        f.close()

        roi_gray = gray[y:y+h, x:x+w]

        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eyes:

            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) 
        
        #mouth_rects = mouth_cascade.detectMultiScale(gray, 1.03, 11)
        
        #for (x,y,w,h) in mouth_rects:
        
         #    y = int(y - 0.15*h)
         
          #   cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
 
           #  break
        

    print "found " +str(len(faces)) +" face(s)"

    cv2.imshow('img',img)

    k = cv2.waitKey(30) & 0xff

    if k == 27:

        break
    end_time=time.time()
    elapsed = end_time - start_time
    if elapsed > 1:
       break

cap.release()

cv2.destroyAllWindows()
