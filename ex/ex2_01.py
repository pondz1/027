import cv2
import numpy as np
# Average filter
filename='../house.tiff'
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale',img)
w,h = img.shape

out1 = np.zeros(img.shape,dtype=np.uint8)
for i in range(1,h-1):
    for j in range(1,w-1):
        out1.itemset((i,j),np.mean(img[i-1:i+2,j-1:j+2]))
cv2.imshow('Average',out1)

# Weight Average filter
mask=np.array([[1,2,1],[2,4,2],[1,2,1]])/16
out2 = np.zeros(img.shape,dtype=np.uint8)
for i in range(1,h-1):
    for j in range(1,w-1):
        out2.itemset((i,j),(mask*(img[i-1:i+2,j-1:j+2])).sum())
cv2.imshow('Weight Average',out2)

cv2.waitKey(0)
cv2.destroyAllWindows()


