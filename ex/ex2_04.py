import cv2
import numpy as np
import matplotlib.pyplot as plt

def equalization(img):
    L=256
    p,bins=np.histogram(img,bins=L,range=(0,L),density=True)
#    p,bins=np.histogram(img,bins=L,range=(0,L))
#    p = cv2.calcHist([img],[0],None,[L],[0,L])
#    P=p.copy()
    out=np.zeros(img.shape,dtype=np.uint8)

##    for j in range(1,L):
##        P[j] = P[j-1]+P[j]
    P=np.cumsum(p)
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            a=int(P[img.item(i,j)]*(L-1))
            out.itemset((i,j),a)

    s,bins=np.histogram(out,bins=L,range=(0,L), density=True)
    S=np.cumsum(s)
    x=list(range(0,L))
    plt.subplot('221')
    plt.plot(x,p)
    plt.title("Histogram")
    
    plt.subplot('223')
    plt.plot(x,P)
    plt.title("Cumulative Histogram")

    plt.subplot('222')
    plt.plot(x,s)
    plt.title("Histogram")
    plt.subplot('224')
    plt.plot(x,S)
    plt.title("Cumulative Histogram")
    plt.show()

    return out.astype(np.uint8)

filename='../pepper.tiff'
#filename='../tank.tiff'
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale',img)

img_eq=equalization(img)

cv2.namedWindow('Image Equalization', cv2.WINDOW_NORMAL)
cv2.imshow('Image Equalization',img_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()


