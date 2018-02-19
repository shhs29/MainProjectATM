import numpy as np
import cv2

N = 1
upper_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

cap = cv2.VideoCapture(0)

def face_detect(body, img, cimg):
	
 	#cv2.imshow('Upper Body',img)
 	faces = face_cascade.detectMultiScale(img, 1.03, 5)
	if len(faces)>0:
		for (x,y,w,h) in faces:
   			cv2.rectangle(cimg,(x,y),(x+w,y+h),(255,0,0),2)
			eyes_detect((x, y, w, h), img, cimg)
                	mouth_detect((x, y, w, h), img, cimg)
	#return cimg

def eyes_detect(faces, img, cimg):
 	    x, y, w, h = faces
    	    roi_gray = img[y:y+h, x:x+w]
    	    eyes = eye_cascade.detectMultiScale(roi_gray)
	    if len(eyes)==0:
           	 print "Error1"
 	    else:
                for a, b, c, d in eyes: 
       			cv2.rectangle(cimg,(a,b),(a+c,b+d),(0,255,0),2)
            	#cv2.imshow('img', cimg)
	    #return cimg
			
def mouth_detect(faces, img, cimg):
   	    x, y, w, h = faces
    	    roi_gray = img[y:y+h, x:x+w]
    	    mouth = mouth_cascade.detectMultiScale(roi_gray)
	    if len(mouth)==0:
           	 print "Error2"
 	    else:
                for a, b, c, d in mouth: 
       			cv2.rectangle(cimg,(a,b),(a+c,b+d),(0,255,0),2)
            #cv2.imshow('img', cimg)
	    

while 1:
 ret, img = cap.read()
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 body = upper_cascade.detectMultiScale(
    gray,
    scaleFactor = 1.01,
    minNeighbors = 5,
    minSize = (30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
)
 if len(body)>0:
	for (x, y, w, h) in body:
    		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face_detect(body, gray, img)	
 else:
 	continue
 

 cv2.imshow('img',img)
 k = cv2.waitKey(30) & 0xff
 if k == 27:
    break
cap.release()
cv2.destroyAllWindows()

   
