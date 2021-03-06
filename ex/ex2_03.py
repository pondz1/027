import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram(img, L=256):
    h = np.zeros(L,dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            h[img.item(i,j)]+=1
    return h

filename='../house.tiff'
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
N=img.size
hist=histogram(img,L=256)/N
print(hist)
x=list(range(0,hist.size))

plt.subplot('221')
plt.plot(x,hist)
plt.title("Histogram")
plt.show()
