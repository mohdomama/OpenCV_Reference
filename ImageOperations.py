import numpy as np
import cv2

img = cv2.imread('me.jpg', cv2.IMREAD_COLOR)

px = img[55,55]
print (px)
img[55,55] = [255, 255, 255]
px = img[55,55]
print(px)

# ROI = Region of Image
ROI = img[100:150, 100:150]
print(ROI)

# img[YaxisRange, XaxisRange]
img[100:300, 300:450] = [255, 255, 255]
my_face = img[40:360,120:365]

img[0:320, 0:245] = my_face
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()