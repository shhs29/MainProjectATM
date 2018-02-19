import cv2
import numpy as np
from matplotlib import pyplot as plt
     
img = cv2.imread('convert.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)
