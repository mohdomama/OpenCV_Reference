import cv2
import numpy as np

img1 = cv2.imread('static/3D-Matplotlib.png')
img2 = cv2.imread('static/mainsvmimage.png')

# add = img1 + img2

# This adds the pixel values
#add = cv2.add(img1, img2)

# The last argument represents Gamma Value
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)


cv2.imshow('Added Image', weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()