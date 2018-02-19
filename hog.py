import cv2
import numpy

def common_data(list1, list2):
    result = False
 
    # traverse in the 1st list
    for x in list1:
 
        # traverse in the 2nd list
        for y in list2:
   
            # if one common
            if x == y:
                result = True
                return result 
                 
    return result
id = 1
id2 = id+1

while id:
  hog1 = cv2.HOGDescriptor()
  hog2 = cv2.HOGDescriptor()
  img1 = "s"+str(id)+".jpg"
  img2 = "s"+ str(id2) +".jpg"
  id+=1
  id2+=1
  if id2==18:
    id=0
  im1 = cv2.imread(img1)
  im2 = cv2.imread(img2)
  h1 = hog1.compute(im1)
  h2 = hog2.compute(im2)
  print h1
  print h2
  if numpy.array_equal(h1,h2):
     print "Shwe"
     id = 0
#print h1
#print h2
#if common_data(h1,h2):
 #print "User 1"
#else:
 #print "Error"
  
#if numpy.allclose(h1,h2):
   

