import numpy as np
import numpy as numpy
import cv2

windowsize_r = 8
windowsize_c = 8

img = cv2.imread('group.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
for r in range(0,gray.shape[0] - windowsize_r, windowsize_r):
  for c in range(0,gray.shape[0] - windowsize_c, windowsize_c):
    window = gray[r:r+windowsize_r,c:c+windowsize_c]
    hist = numpy.histogram(window,bins=256)
#plt.hist(myarray, normed=True)
cv2.imshow('wind',window)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
