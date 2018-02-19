import numpy as np

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 1
fontColor = (255, 255, 255)

cap = cv2.VideoCapture(0)


while 1:

    ret, img = cap.read()
   
    locy = int(img.shape[0]/2) # the text location will be in the middle
    locx = int(img.shape[1]/2) #           of the frame for this example   

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.5, 5)

    for (x,y,w,h) in faces:
         
        mouth_rects = mouth_cascade.detectMultiScale(gray, 1.03, 11)
        if len(mouth_rects)==0:
            cv2.putText(img, "Mouth covered", (locx, locy), fontFace, fontScale, fontColor)

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray = gray[y:y+h, x:x+w]

        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eyes:

            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) 
        
   
     
        
        for (x,y,w,h) in mouth_rects:
        
             y = int(y - 0.15*h)
         
             cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
 
           #  break
       

    print "found " +str(len(faces)) +" face(s)"
    
   # if len(faces)>4:
    #    cv2.putText(img, "Warning: Threshold reached", (locx, locy), fontFace, fontScale, fontColor) 
    #else:
     #   cv2.putText(img, "Found "+str(len(faces))+" face(s)", (locx, locy), fontFace, fontScale, fontColor) 
    cv2.imshow('img',img)

    k = cv2.waitKey(30) & 0xff

    if k == 27:

        break

cap.release()

cv2.destroyAllWindows()
