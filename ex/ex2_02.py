import cv2
import numpy as np
# Median filter 3x3
def medianFilter(img,n=3):
    w,h = img.shape
    out = np.zeros(img.shape,dtype=np.uint8)
    beg=n//2
    end=beg+1
    print(beg,end)
    for i in range(beg,h-beg):
        for j in range(beg,w-beg):
            out.itemset((i,j),np.median(img[i-beg:i+end,j-beg:j+end]))
    return out

filename='../airplane_sp.png'
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Grayscale', cv2.WINDOW_NORMAL)
cv2.imshow('Grayscale',img)
cv2.namedWindow('Median 3x3', cv2.WINDOW_NORMAL)
cv2.imshow('Median 3x3',medianFilter(img,n=3))
cv2.namedWindow('Median 5x5', cv2.WINDOW_NORMAL)
cv2.imshow('Median 5x5',medianFilter(img,n=5))
cv2.namedWindow('Median 7x7', cv2.WINDOW_NORMAL)
cv2.imshow('Median 7x7',medianFilter(img,n=7))
cv2.waitKey(0)
cv2.destroyAllWindows()


