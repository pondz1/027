import cv2
import numpy as np
# Average filter
filename='../misc/house.tiff'
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Laplacian', cv2.WINDOW_NORMAL)
cv2.imshow('Laplacian',img)
w,h = img.shape
# Weight Average filter
mask=np.array([[0,0,-1,0,0],[0,-1,-2,-1,0],[-1,-2,16,-2,-1],[0,-1,-2,-1,0],[0,0,-1,0,0]])
#mask=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
n=mask.shape[0]
#out = np.zeros(img.shape,dtype=np.uint8)
out2 = img.copy()
beg=n//2
end=beg+1
print(beg,end)
for i in range(beg,h-beg):
    for j in range(beg,w-beg):
        sub=img[i-beg:i+end,j-beg:j+end]
        re=(mask*sub).sum()
        if re<0 or re>255:
            if re<0:
                re=0
            else:
                re=255         
        out2.itemset((i,j),re)
print(out2)
cv2.namedWindow('Laplacian', cv2.WINDOW_NORMAL)
cv2.imshow('Laplacian',out2)

cv2.waitKey(0)
cv2.destroyAllWindows()


