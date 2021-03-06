# add operation
import cv2
import numpy as np
import matplotlib.pyplot as plt

filename='../Mandrill.BMP'
#filename='../shirt1.jpg'
img = cv2.imread(filename)
cv2.namedWindow('Image1', cv2.WINDOW_NORMAL)
cv2.imshow('Image1',img)
#mask = cv2.imread('../lena512color.tiff')
#mask = cv2.imread('../house.tiff')
mask=np.ones(img.shape,dtype=np.uint8)*64
cv2.namedWindow('Image2', cv2.WINDOW_NORMAL)
cv2.imshow('Image2',mask)

#im_add=cv2.add(img,mask)
h,w=mask.shape[0],mask.shape[1]
im_add=img.copy()
for i in range(h):
    for j in range(w):
        im_add[i,j]=img[i,j]+mask[i,j]

cv2.namedWindow('ADD', cv2.WINDOW_NORMAL)
cv2.imshow('ADD',im_add)
cv2.waitKey(0)
cv2.destroyAllWindows()
