# Logical Operator
import cv2
import numpy as np

filename='../F1.tiff'
img = cv2.imread(filename,0)
cv2.namedWindow('Grayscale', cv2.WINDOW_NORMAL)
cv2.imshow('Grayscale',img)
h,w=img.shape
q=int(h/4)
mask1=np.zeros(img.shape, dtype=np.uint8)
mask2=np.ones(img.shape, dtype=np.uint8)*255
im_and=im_or=mask1.copy()
for i in range(q,h-q):
    for j in range(q,int(w-q/2)):
        mask1.itemset((i,j),255)
        mask2.itemset((i,j),0)
       
cv2.namedWindow('Mask AND', cv2.WINDOW_NORMAL)
cv2.imshow('Mask AND',mask1)
cv2.bitwise_and(img,mask1,im_and)
cv2.namedWindow('AND', cv2.WINDOW_NORMAL)
cv2.imshow('AND',im_and)
cv2.namedWindow('Mask OR', cv2.WINDOW_NORMAL)
cv2.imshow('Mask OR',mask2)
cv2.bitwise_or(img,mask2,im_or)
cv2.namedWindow('OR', cv2.WINDOW_NORMAL)
cv2.imshow('OR',im_or)
cv2.waitKey(0)
cv2.destroyAllWindows()

##plt.figure(1)
##plt.subplot('131')
##plt.axis('off')
##plt.title('Grayscale')
##plt.imshow(img,cmap="gray")

##plt.figure(1)
##plt.subplot('131')
##plt.axis('off')
##plt.title('Grayscale')
##plt.imshow(img,cmap="gray")


##cv2.bitwise_and(img,mask1,im_and)
##cv2.bitwise_or(img,mask2,im_or)
##plt.subplot('232')
##plt.axis('off')
##plt.title('Mask And')
##plt.imshow(mask1,cmap="gray")
##plt.subplot('233')
##plt.axis('off')
##plt.title('And')
##plt.imshow(im_and,cmap="gray")
##
##plt.subplot('235')
##plt.axis('off')
##plt.title('Mask OR')
##plt.imshow(mask2,cmap="gray")
##plt.subplot('236')
##plt.axis('off')
##plt.title('OR')
##plt.imshow(im_or,cmap="gray")
##

