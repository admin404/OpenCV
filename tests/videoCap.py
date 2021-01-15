import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0)

while(True):
    ret,frame = vid.read()
    cv.imshow("My cam video", frame)

    if cv.waitKey(1) &0XFF == ord('q'):
        break

vid.release()    
cv.waitKey(0)
