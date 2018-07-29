import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	
	_, frame = cap.read()
	
	cv2.imshow('Original',frame)
	# cv2.Canny(frame, size, size). More size =  More noise
	# There are other edge detectors avaiable as well.
	edges = cv2.Canny(frame,100,150)
	cv2.imshow('Edges',edges)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()