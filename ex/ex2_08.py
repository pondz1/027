# Image subtraction
import cv2
import numpy as np

#filename='../Mandrill.BMP'
filename='../s047.tif'
#filename='../shirt1.jpg'
img = cv2.imread(filename,0)
cv2.namedWindow('Image1', cv2.WINDOW_NORMAL)
cv2.imshow('Image1',img)
#mask = cv2.imread('../shirt2.jpg')
#mask = cv2.imread('../lena512color.tiff')
mask = np.ones(img.shape,dtype=np.uint8)*64
#mask = np.zeros(img.shape,dtype=np.uint8)
cv2.namedWindow('Image2', cv2.WINDOW_NORMAL)
cv2.imshow('Image2',mask)

im_sub=cv2.subtract(img,mask)

cv2.namedWindow('Subtract', cv2.WINDOW_NORMAL)
cv2.imshow('Subtract',im_sub)
cv2.waitKey(0)
cv2.destroyAllWindows()
