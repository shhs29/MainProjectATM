from __future__ import print_function
import cv2
import os, sys
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
import pickle
import shutil

######database######
import mysql.connector
from mysql.connector import errorcode
#####main function####
DB_NAME = 'users'

cnx = mysql.connector.connect(user='root', password='kizhakkaneth',
                              database='users')
cursor = cnx.cursor()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 1
fontColor = (255, 255, 255)

sampleN=0;
path = 'dataset1/s'
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
frame_set=[]

while 1:
        
	ret, img = cap.read()

	locy = int(img.shape[0]/2) # the text location will be in the middle
	
	locx = int(img.shape[1]/2) #           of the frame for this example 
	
	now = time.time()

	future = now + 100

	f = open('store.pckl', 'rb')

	id = pickle.load(f)
		
	f.close()

	os.mkdir(path + str(id), 0755)

	query_insert = "insert into userdata VALUES('User" + str(id) + "','s" + str(id) + "',1);"

	cursor.execute(query_insert)

	cnx.commit()

	i = 1
   
 	while time.time() < future:

		ret, img = cap.read()
      
	        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

		if i==1: 

			i = 0

			cv2.imwrite("user.jpg", img)

			os.system("python detection.py")

			f = open('name.pckl', 'rb')

			name = pickle.load(f)
		
			f.close()

			if "Unknown" not in name:

				sampleValue = 1

				shutil.rmtree(path + str(id))
			
				query_delete = "delete from userdata where name='User"+str(id)+"'";

				cursor.execute(query_delete)

				cnx.commit()

				query_change = "update userdata set frequency=frequency+1 where image='"+name+"';"

				cursor.execute(query_change)

				cnx.commit()

				id=id-1	


			else:

				sampleValue = 0	
	     
		if sampleValue==0:                
		
			if sampleN >= 40:

				sampleN = 0

				break
	    
			else:	
				
				for (x,y,w,h) in faces:
	                               
					#cv2.imwrite("user.jpg", img)

					#os.system("python detection.py")
				
					f = open('name.pckl', 'rb')
	
					label_text = pickle.load(f)
		
					f.close()	        

					sampleN=sampleN+1;

					now1 = datetime.datetime.now()

			        	cv2.imwrite(path + str(id) + "/User."+ str(id) + "." +str(sampleN) + str(now1) + ".jpg", gray)
		
			        	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	
	        			roi_gray = gray[y:y+h, x:x+w]

	        			roi_color = img[y:y+h, x:x+w]

	        			eyes = eye_cascade.detectMultiScale(roi_gray)

	        			for (ex,ey,ew,eh) in eyes:

	                			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) 

			        		cv2.waitKey(50)
	
			        		cv2.imshow('img',img)
			
				if len(faces)>1:

	    				cv2.putText(img, "Warning: Threshold reached", (locx, locy), fontFace, fontScale, fontColor) 
	
					print("Warning: Threshold reached")
    		
				else:

	        			cv2.putText(img, "Found "+str(len(faces))+" face(s)", (locx, locy), fontFace, fontScale, fontColor) 

					print("Found "+str(len(faces))+" face(s)")		

				cv2.waitKey(100)

				cv2.imshow('img',img)

	id+=1
        	
	f = open('store.pckl', 'wb')
        	
	pickle.dump(id, f)
	
	f.close()

	print("Time exceeded")

	#break
   
    	cv2.waitKey(1)
  			
		
	cv2.waitKey(100) 

	cv2.imshow('img',img)
		

	

	#if k == 27:

		#break

cap.release()

cv2.destroyAllWindows()

