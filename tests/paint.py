import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

blank[200:300, 300:200] = 0,0,255

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)

cv.circle(blank, (blank.shape[1]//2, blank.shape[1]//2), 40, (0,0,255), thickness = -1)

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness = 3)
cv.imshow('Paint', blank)

cv.waitKey(0)
