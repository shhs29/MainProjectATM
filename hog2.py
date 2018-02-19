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

hog1 = cv2.HOGDescriptor()
hog2 = cv2.HOGDescriptor()
im1 = cv2.imread("abhi.jpg")
im2 = cv2.imread("abhi2.jpg")
h1 = hog1.compute(im1)
h2 = hog2.compute(im2)
#xx = h1.reshape(2, -1)
#yy = h2.reshape(2, -1)
#dist = np.hypot(*(xx - yy))

#print dist
#diff = numpy.subtract(h1,h2)
#print diff
print h1
print h2
if numpy.array_equal(h1,h2):
  print "User 1"
   
#print h1
#print h2
#if common_data(h1,h2):
 #print "User 1"
#else:
 #print "Error"
  
#if numpy.allclose(h1,h2):
   
