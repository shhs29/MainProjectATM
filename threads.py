import numpy as np
import cv2
import threading
import os

def function1(img):
 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    body = upper_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.01,
        minNeighbors = 5,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in body:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    faces = face_cascade.detectMultiScale(gray, 1.03, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        mouth_rects = mouth_cascade.detectMultiScale(gray, 1.7, 11)
        for (x,y,w,h) in mouth_rects:
            y = int(y - 0.15*h)
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
            break
    cv2.imshow('img',img)

if __name__=='__main__':
    upper_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

    cap = cv2.VideoCapture('video.mp4')
    while 1:
        ret, img = cap.read()
        t1 = threading.Thread(target = function1, args=(img,))
        t1.start()
        t1.join()
    cap.release()
    cv2.destroyAllWindows()
