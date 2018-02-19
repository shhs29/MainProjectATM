import os

import numpy as np

import cv2

from PIL import Image # For face recognition we will the the LBPH Face Recognizer 

recognizer = cv2.face.LBPHFaceRecognizer_create()

path="/home/shweta/Documents"

def getImagesWithID(path):

    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]   

 # print image_path   

 #getImagesWithID(path)

    faces = []

    IDs = []

    for imagePath in imagePaths:      

  # Read the image and convert to grayscale

        facesImg = Image.open(imagePath).convert('L')

        faceNP = np.array(facesImg, 'uint8')

        # Get the label of the image
        try :
          ID = (os.path.split(imagePath)[-1].split(".")[1])
          ID = map(float, ID)
         # Detect the face in the image
        except :
          print imagePath
          break 

        faces.append(faceNP)

        IDs.append(ID)

        cv2.imshow("Adding faces for traning",faceNP)

        cv2.waitKey(10)

    return np.array(IDs), faces

Ids,faces  = getImagesWithID(path)

recognizer.train(faces,Ids)

recognizer.save("trainingdata.yml")

cv2.destroyAllWindows()
