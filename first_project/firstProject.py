import cv2 as cv
import imutils
import numpy as np

image = cv.imread("rosemary_greg2.jpg")
   ...: image=imutils.resize(image,width=500)
   ...: image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
   ...: 
   ...: # cv.imshow('gray',image)
   ...: 
   ...: thrsh=np.array([100,255])
   ...: edged = cv.Canny(image, thrsh[0], thrsh[1],apertureSize=3);
   ...: 
   ...: # binaryImage=np.uint8(image<100)*255
   ...: 
   ...: edged[407:,:]=0
   ...: edged[:,165:]=0
   ...: 
   ...: 
   ...: points=np.where(edged>0)
