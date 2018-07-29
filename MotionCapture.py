'''
It is called background reductions
'''

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(history=50, varThreshold=15 ,detectShadows=False)

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    
    smooth = cv2.medianBlur(fgmask,15)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',fgmask)
    cv2.imshow('smooth', smooth)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()