'''
Tranparent logo imposed on image
'''

import cv2
import numpy as np

img = cv2.imread('static/3D-Matplotlib.png')
logo = cv2.imread('static/mainlogo.png')

# Convert Logo from 3 channel to 1 channel for easy modifications
logo_grey = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

row, col, channels = logo.shape

roi = img[0:row, 0:col]

# Create mask
ret, mask = cv2.threshold(logo_grey, 240, 255, cv2.THRESH_BINARY_INV)

# Invert mask
mask_inv = cv2.bitwise_not(mask)

# Make background transparent (black)
logo_trans = cv2.bitwise_and(logo, logo, mask = mask)

# Get the logoless area of ROI
back = cv2.bitwise_and(roi, roi, mask = mask_inv)

# Add the two to get the illusion of transparent logo
logo_out = cv2.add(back, logo_trans)

# Impose logo on original image
img[0:row, 0:col] = logo_out

cv2.imshow('Image With Transparent Logo', img)


cv2.waitKey(0)
cv2.destroyAllWindows()