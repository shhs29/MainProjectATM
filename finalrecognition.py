import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create();
rec.read("trainer/trainer.yml")
id=0
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 1
fontColor = (255, 255, 255)

ret, img = cap.read()
locy = int(img.shape[0]/2) # the text location will be in the middle
locx = int(img.shape[1]/2) #           of the frame for this example

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(id==2):
            id="peter"
        if id==1:
            id="shweta"
        if id==3:
            id="anjali"
        if id==4:
            id="Gaurav"
       
        #cv2.PutText(cv2.fromarray(img),str(id),(x,y+h),font,255)
        cv2.putText(img, str(id), (locx, locy), fontFace, fontScale, fontColor) 
    cv2.imshow('img',img)
    
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()
