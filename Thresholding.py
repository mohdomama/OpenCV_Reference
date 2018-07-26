import cv2
import numpy as np

img = cv2.imread('static/bookpage.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret1, thresh_orig = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
ret2, thresh_gray = cv2.threshold(img_gray, 12, 255, cv2.THRESH_BINARY)

# A better way of thresholding. There are other ways as well.
thresh_adap = cv2.adaptiveThreshold(
	img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('original', img)
cv2.imshow('thresh_orig', thresh_orig)
cv2.imshow('thresh_gray', thresh_gray)
cv2.imshow('thresh_adap', thresh_adap)

cv2.waitKey(0)
cv2.destroyAllWindows()